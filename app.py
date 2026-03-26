import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Trading Dashboard",
    layout="wide"
)

st.title("📈 Trading Dashboard")

# Fake data pour test
np.random.seed(42)
price = np.cumsum(np.random.randn(100)) + 100

df = pd.DataFrame({
    "price": price
})

# Layout
col1, col2, col3 = st.columns(3)

col1.metric("PnL", "$125.32", "+2.4%")
col2.metric("Position", "LONG")
col3.metric("Risk", "0.5%")

# Graph
fig = go.Figure()

fig.add_trace(go.Scatter(
    y=df["price"],
    mode='lines',
    name='Price'
))

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Logs")
st.write("Bot démarré...")