import numpy as np
import pandas as pd


def moving_average_crossover(
    df: pd.DataFrame, fast_window: int = 20, slow_window: int = 50 ) -> pd.DataFrame:
    """
        - Buy Signal (1): Fast SMA crosses above Slow SMA 
        - Sell Signal (-1): Fast SMA crosses below Slow SMA 

    Returns:
        pd.DataFrame: DataFrame with SMAs, regime positions, and trade signals.
    """
    data = df.copy()

    data["fast_sma"] = data["Close"].rolling(window=fast_window).mean()
    data["slow_sma"] = data["Close"].rolling(window=slow_window).mean()

    
    data["position"] = np.where(data["fast_sma"] > data["slow_sma"], 1, 0)

    # 3. Generate Signal Crossovers (+1 Buy, -1 Sell, 0 Hold)
    data["signal"] = data["position"].diff().fillna(0)

    return data

def relative_strength_index(df: pd.DataFrame, window: int = 14, oversold_threshold: float = 30.0, overbought_threshold: float = 70.0, ) -> pd.DataFrame:
    """
        - Buy Signal (1): RSI crosses above oversold threshold (e.g., 30).
        - Sell Signal (-1): RSI crosses below overbought threshold (e.g., 70).

       Returns:
        pd.DataFrame: DataFrame with RSI values, positions, and trade signals.
    """
    data = df.copy()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / window, min_periods=window, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / window, min_periods=window, adjust=False).mean()

    
