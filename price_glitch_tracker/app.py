import streamlit as st
import pandas as pd
import yaml
import os
from datetime import datetime

st.set_page_config(page_title="Price Glitch Tracker", layout="wide")

# Load product list
@st.cache_data
def load_products():
    if not os.path.exists("products.csv"):
        return pd.DataFrame(columns=["url", "threshold"])
    return pd.read_csv("products.csv")

# Load config
@st.cache_data
def load_config():
    if not os.path.exists("config.yaml"):
        return {"interval_minutes": 5, "discord_webhook": ""}
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

products_df = load_products()
config = load_config()

st.title("🛍️ Price Glitch Tracker Dashboard")

st.subheader("🔗 Tracked Products")
st.dataframe(products_df)

st.subheader("⚙️ Config")
st.json(config)

st.info("This is a front-end dashboard only. Run `python main.py` in your terminal to start live tracking.", icon="ℹ️")