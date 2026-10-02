import streamlit as st
from engine.data_fetcher import get_stock_data
from engine.strategies import moving_average_crossover

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
