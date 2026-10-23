import streamlit as st
from engine.data_fetcher import get_stock_data
from engine.strategies import moving_average_crossover
from engine.strategies import rsi_strategy
from engine.strategies import bollinger_bands

#page setup
st.set_page_config(page_title="QuantDeck Dashboard", layout="wide")
st.title("QuantDeck Test")

#side bar and parameters
st.sidebar.header("Configuration")
ticker = st.sidebar.selectbox("Ticker Symbol", TICKER_LIST, index=TICKER_LIST.index("AAPL") if "AAPL" in TICKER_LIST else 0)
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-01-01"))
st.sidebar.subheader("Strategy Selection")
strategy_name = st.sidebar.selectbox("Choose Strategy", list(STRATEGIES.keys()))

#dynamic strategy parameters
strat_params = {}
if strategy_name == "Moving Average Crossover":
    strat_params["fast"] = st.sidebar.slider("Fast SMA Window", min_value=5, max_value=50, value=20)
    strat_params["slow"] = st.sidebar.slider("Slow SMA Window", min_value=20, max_value=200, value=50)
elif strategy_name == "RSI":
    strat_params["period"] = st.sidebar.slider("RSI Period", min_value=5, max_value=30, value=14)
    strat_params["oversold"] = st.sidebar.slider("Oversold Level", min_value=10, max_value=40, value=30)
    strat_params["overbought"] = st.sidebar.slider("Overbought Level", min_value=60, max_value=90, value=70)
elif strategy_name == "Bollinger Bands":
    strat_params["window"] = st.sidebar.slider("BB Window", min_value=10, max_value=50, value=20)
    strat_params["num_std"] = st.sidebar.slider("Standard Deviations", min_value=1.0, max_value=3.0, value=2.0, step=0.5)

#capital and commission
st.sidebar.subheader("Backtest Settings")
initial_cash = st.sidebar.number_input("Initial Cash ($)", value=10000.0, step=1000.0)
commission_pct = st.sidebar.number_input("Commission (%)", value=0.0, step=0.01)


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
