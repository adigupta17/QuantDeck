import pandas as pd
import yfinance as yf
import streamlit as st


@st.cache_data(ttl=3600)
#fetch historical OHLCV equity data, sanitize missing values
def get_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if data.empty:
            raise ValueError(f"No market data retrieved for ticker '{ticker}'.")

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
      
        data = data.ffill().bfill()
 
        required_cols = ["Open", "High", "Low", "Close", "Volume"]
        data = data[required_cols]

        return data

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame()
