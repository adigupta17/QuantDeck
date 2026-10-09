from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class StrategyResult:
    position: pd.Series
    overlays: dict = field(default_factory=dict)  
    panel: dict | None = None                     

def sma_crossover(df, fast=20, slow=50) -> StrategyResult:
    if fast >= slow:
        raise ValueError("Fast window must be smaller than slow window.")
    f = df["Close"].rolling(fast).mean()
    s = df["Close"].rolling(slow).mean()
    pos = ((f > s) & f.notna() & s.notna()).astype(int)
    return StrategyResult(pos, {f"SMA {fast}": f, f"SMA {slow}": s})


def rsi_series(close: pd.Series, period=14) -> pd.Series:
    """Wilder's RSI."""
    d = close.diff()
    gain = d.clip(lower=0).ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    loss = (-d.clip(upper=0)).ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    rsi = 100 - 100 / (1 + gain / loss)
    return rsi.where(~((loss == 0) & gain.notna()), 100.0)


def rsi_strategy(df, period=14, oversold=30, overbought=70) -> StrategyResult:
    if oversold >= overbought:
        raise ValueError("Oversold level must be below overbought level.")
    rsi = rsi_series(df["Close"], period)
    held, out = 0, []
    for v in rsi.to_numpy():
        if not np.isnan(v):
            if held == 0 and v < oversold:
                held = 1
            elif held == 1 and v > overbought:
                held = 0
        out.append(held)
    return StrategyResult(
        pd.Series(out, index=df.index), panel={"name": "RSI", "series": rsi, "levels": [oversold, overbought]}
    )


def bollinger_bands(df, window=20, num_std=2.0, exit_at="Middle band") -> StrategyResult:
    """Buy when close drops below the lower band; sell at the middle (or upper) band."""
    c = df["Close"]
    mid = c.rolling(window).mean()
    sd = c.rolling(window).std()
    upper, lower = mid + num_std * sd, mid - num_std * sd
    exit_line = mid if exit_at == "Middle band" else upper
    held, out = 0, []
    for price, lo, ex in zip(c.to_numpy(), lower.to_numpy(), exit_line.to_numpy()):
        if not np.isnan(lo):
            if held == 0 and price < lo:
                held = 1
            elif held == 1 and price > ex:
                held = 0
        out.append(held)
    return StrategyResult(
        pd.Series(out, index=df.index), {"Upper band": upper, "Middle band": mid, "Lower band": lower}
    )


STRATEGIES = {
    "Moving Average Crossover": sma_crossover,
    "RSI": rsi_strategy,
    "Bollinger Bands": bollinger_bands,
}
