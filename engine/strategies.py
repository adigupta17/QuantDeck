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


