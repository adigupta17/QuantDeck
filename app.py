from datetime import date, timedelta

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from quantdeck import theme as T
from quantdeck.backtester import run_backtest
from quantdeck.data import fetch_prices
from quantdeck.metrics import TRADING_DAYS, compute_metrics
from quantdeck.strategies import STRATEGIES

PERIODS = {"1Y": 365, "3Y": 3 * 365, "5Y": 5 * 365}
WARMUP_DAYS = 450  # extra history so indicators are ready on the first day shown
H = 300

st.set_page_config(page_title="QuantDeck", page_icon="📈", layout="wide")
st.markdown(T.CSS, unsafe_allow_html=True)


@st.cache_data(show_spinner="Fetching data…")
def load(ticker, start, end):
    return fetch_prices(ticker, start, end)

#sidebar
sb = st.sidebar


def label(text):
    sb.markdown(f'<div class="sec">{text}</div>', unsafe_allow_html=True)


label("Market")
ticker = sb.text_input("Ticker symbol", "AAPL", max_chars=10).upper().strip()
bench_t = sb.text_input("Benchmark", "SPY", max_chars=10).upper().strip()

label("Time period")
if hasattr(st, "segmented_control"):
    period = sb.segmented_control("Period", list(PERIODS), default="3Y", label_visibility="collapsed") or "3Y"
else:
    period = sb.radio("Period", list(PERIODS), index=1, horizontal=True, label_visibility="collapsed")

label("Initial investment")
cash0 = sb.number_input("Amount ($)", min_value=100, max_value=10_000_000, value=10_000, step=1_000)
fee = sb.number_input("Commission per trade (%)", 0.0, 5.0, 0.0, step=0.05)

label("Strategy")
name = sb.selectbox("Strategy", list(STRATEGIES), label_visibility="collapsed")

label("Parameters")
# Ranges for paired parameters never overlap, so they can never be equal.
if name == "Moving Average Crossover":
    params = dict(fast=sb.slider("Fast SMA (days)", 5, 49, 20),
                  slow=sb.slider("Slow SMA (days)", 50, 250, 50))
    sb.caption("Fast range (5–49) stays below slow range (50–250).")
elif name == "RSI":
    params = dict(period=sb.slider("RSI period (days)", 5, 30, 14),
                  oversold=sb.slider("Oversold – buy below", 10, 45, 30),
                  overbought=sb.slider("Overbought – sell above", 55, 90, 70))
    sb.caption("Oversold (10–45) always stays below overbought (55–90).")
else:
    params = dict(window=sb.slider("Window (days)", 10, 60, 20),
                  num_std=sb.slider("Std deviations", 1.0, 3.5, 2.0, 0.1),
                  exit_at=sb.radio("Sell when price crosses", ["Middle band", "Upper band"]))


