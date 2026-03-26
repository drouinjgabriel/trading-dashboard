import nest_asyncio
nest_asyncio.apply()

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.broker.ibkr import connect_ib, get_ticker
import time


st.set_page_config(layout="wide")

st.title("📈 Trading Dashboard (IBKR LIVE)")

# --- CONNECT ---
ib = connect_ib()
ticker = get_ticker("AAPL")

# --- WAIT DATA ---
ib.sleep(2)

price = ticker.last if ticker.last else ticker.close
bid = ticker.bid if ticker.bid else 0
ask = ticker.ask if ticker.ask else 0
spread = ask - bid

# --- UI ---
col1, col2, col3, col4 = st.columns(4)

col1.metric("Last", f"{price:.2f}")
col2.metric("Bid", f"{bid:.2f}")
col3.metric("Ask", f"{ask:.2f}")
col4.metric("Spread", f"{spread:.4f}")

# --- HISTORY ---
if "prices" not in st.session_state:
    st.session_state.prices = []

if price:
    st.session_state.prices.append(price)

df = pd.DataFrame(st.session_state.prices, columns=["price"])

# --- GRAPH ---
fig = go.Figure()
fig.add_trace(go.Scatter(y=df["price"], mode="lines"))

fig.update_layout(template="plotly_dark", height=500)

st.plotly_chart(fig, use_container_width=True)

st.write("Live data from IBKR 🚀")

# --- AUTO REFRESH ---
time.sleep(1)
st.rerun()