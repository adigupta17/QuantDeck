from datetime import date
from pathlib import Path
import pandas as pd

CACHE_DIR = Path(__file__).resolve().parent.parent / "data_cache"
OHLC = ["Open", "High", "Low", "Close"]


#Remove anomalies like duplicates, unsorted dates, non-positive prices, and NaN values
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[~df.index.duplicated(keep="first")].sort_index()
    df = df.dropna(subset=OHLC)
    df = df[(df[OHLC] > 0).all(axis=1)]
    return df


#Daily OHLCV
def fetch_prices(ticker: str, start: date, end: date, use_cache: bool = True) -> pd.DataFrame:
    ticker = ticker.strip().upper()
    if not ticker:
        raise ValueError("Please enter a ticker.")
    CACHE_DIR.mkdir(exist_ok=True)
    path = CACHE_DIR / f"{ticker}_{start}_{end}.csv"

    if use_cache and path.exists():
        df = pd.read_csv(path, index_col=0, parse_dates=True)
    else:
        import yfinance as yf  
        
        df = yf.download(ticker, start=str(start), end=str(end), auto_adjust=True, progress=False)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        if df.empty:
            raise ValueError(f"No data found for '{ticker}'. Check the ticker and date range.")
        df = df[["Open", "High", "Low", "Close", "Volume"]]
        df.index = pd.to_datetime(df.index).tz_localize(None)
        df.to_csv(path)

    df = clean_data(df)
    if df.empty:
        raise ValueError(f"No usable data for '{ticker}' in that range.")
    return df

