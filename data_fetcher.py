import yfinance as yf
import pandas as pd

def fetch_stock_data(stock, period):
    df = yf.download(stock, period=period, interval="1d", progress=False)

    if df is None or df.empty:
        return None, f"⚠️ No data found for {stock}. Skipping."

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    if "Close" not in df.columns:
        return None, f"⚠️ 'Close' column missing for {stock}. Skipping."

    df = df.dropna(subset=["Close"])

    if len(df) < 5:
        return None, f"⚠️ Not enough valid data for {stock}. Skipping."

    return df, None
