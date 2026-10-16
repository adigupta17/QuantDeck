#All in All out approach
import numpy as np
import pandas as pd


def run_backtest(df: pd.DataFrame, position: pd.Series, initial_cash=10_000.0, commission_pct=0.0):
    
    fee = commission_pct / 100.0
    target = position.reindex(df.index).shift(1).fillna(0).astype(int).to_numpy()
    cash, shares, entry_cost = float(initial_cash), 0, 0.0
    equity, trades = [], []

    for i, (day, row) in enumerate(df.iterrows()):
        px = row["Open"]
        if target[i] == 1 and shares == 0:
            n = int(cash // (px * (1 + fee)))
            if n > 0:
                cost, f = n * px, n * px * fee
                cash -= cost + f
                shares, entry_cost = n, cost + f
                trades.append(dict(Date=day, Action="BUY", Price=px, Shares=n, Fee=f, Cash=cash, PnL=np.nan))
        elif target[i] == 0 and shares > 0:
            proceeds, f = shares * px, shares * px * fee
            cash += proceeds - f
            trades.append(dict(Date=day, Action="SELL", Price=px, Shares=shares, Fee=f, Cash=cash,
                               PnL=proceeds - f - entry_cost))
            shares, entry_cost = 0, 0.0
        equity.append(cash + shares * row["Close"])

    cols = ["Date", "Action", "Price", "Shares", "Fee", "Cash", "PnL"]
    return pd.Series(equity, index=df.index, name="Equity"), pd.DataFrame(trades, columns=cols)
