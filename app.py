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


#header
st.markdown(
    f'<div class="topbar"><span class="brand">QUANTDECK · STRATEGY BACKTESTER</span>'
    f'<span class="badge">{ticker or "—"}</span><span class="badge">{name}</span>'
    f'<span class="badge">vs {bench_t or "—"}</span><span class="badge">{period}</span>'
    f'<span class="badge">All-In / All-Out</span></div>', unsafe_allow_html=True)

#compute 
try:
    end = date.today()
    start = end - timedelta(days=PERIODS[period])
    raw = load(ticker, start - timedelta(days=WARMUP_DAYS), end)
    bench_raw = load(bench_t, start - timedelta(days=WARMUP_DAYS), end)

    res = STRATEGIES[name](raw, **params)
    df, bench = raw.loc[pd.Timestamp(start):], bench_raw.loc[pd.Timestamp(start):]
    if len(df) < 30:
        raise ValueError("Not enough data in this period (need at least 30 trading days).")

    equity, trades = run_backtest(df, res.position, cash0, fee)
    bench_eq, _ = run_backtest(bench, pd.Series(1, index=bench.index), cash0, fee)
    bench_eq = bench_eq.reindex(equity.index).ffill().bfill()
except Exception as e:
    st.error(f"error {e}")
    st.stop()

sm, bm = compute_metrics(equity, trades), compute_metrics(bench_eq)

#kpi strip
pct = lambda v: "—" if pd.isna(v) else f"{v:+.1%}" if abs(v) < 10 else f"{v:+.0%}"
tone = lambda v: "pos" if v > 0 else "neg" if v < 0 else ""
kpis = [
    ("Total return", pct(sm["Total Return"]), "big", f"{bench_t}: {pct(bm['Total Return'])}"),
    ("Sharpe ratio", f"{sm['Sharpe Ratio']:.2f}", "", f"{bench_t}: {bm['Sharpe Ratio']:.2f}"),
    ("Max drawdown", f"{sm['Max Drawdown']:.1%}", "neg", f"{bench_t}: {bm['Max Drawdown']:.1%}"),
    ("CAGR", pct(sm["Annualized Return (CAGR)"]), tone(sm["Annualized Return (CAGR)"]),
     f"{bench_t}: {pct(bm['Annualized Return (CAGR)'])}"),
    ("Win rate", "—" if pd.isna(sm["Win Rate"]) else f"{sm['Win Rate']:.0%}", "", "closed trades"),
    ("Trades", f"{sm['Completed Trades']}", "", "round trips"),
    ("Final value", f"${sm['Final Value']:,.0f}", "", f"{bench_t}: ${bm['Final Value']:,.0f}"),
]