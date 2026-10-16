import streamlit as st
from engine.data_fetcher import get_stock_data
from engine.strategies import moving_average_crossover
from engine.strategies import rsi_strategy
from engine.strategies import bollinger_bands

#page setup
st.set_page_config(page_title="QuantDeck Dashboard", layout="wide")
st.title("QuantDeck Test")

#side bar and parameters
st.sidebar.header("Strategy Configuration")
ticker = st.sidebar.text_input("Ticker Symbol", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-01-01"))
st.sidebar.subheader("SMA Crossover Parameters")
fast_win = st.sidebar.slider("Fast SMA Window", min_value=5, max_value=50, value=20)
slow_win = st.sidebar.slider("Slow SMA Window", min_value=20, max_value=200, value=50)

#fetch data
if st.sidebar.button("Run Strategy"):
    with st.spinner("Fetching market data..."):
        df = get_stock_data(ticker, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

    if not df.empty:
        #moving average crossover strategy
        results = moving_average_crossover(df, fast_window=fast_win, slow_window=slow_win)

        st.subheader(f"Strategy Results: {ticker}")
        st.line_chart(results[["Close", "fast_sma", "slow_sma"]])

        #display signal data
        st.subheader("Data Preview & Signals")
        st.dataframe(results.tail(15))

        #RSI strategy
        result = rsi_strategy(df, period=14, oversold=30, overbought=70)
        positions = result.position
        rsi_data = result.panel["series"]
        print(result.panel["levels"])  

        #bollinger bands strategy
        result = bollinger_bands(df, window=20, num_std=2.0, exit_at="Middle band")
        positions = result.position
        upper_band = result.overlays["Upper band"]
        middle_band = result.overlays["Middle band"]
        lower_band = result.overlays["Lower band"]


    else:
        st.error("Failed to load ticker data. Check symbol or date range.") 
