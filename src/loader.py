import os
import yfinance as yf
import pandas as pd
from src.config import TICKERS, START_DATE, END_DATE

DATA_DIR = "data"
CACHE_FILE = os.path.join(DATA_DIR, "stock_prices.csv")

def load_stock_data(force_download=False):
    """
    Load data, lalu hitung Daily Log Returns.
    """
    # --- 1. LOAD DATA ---
    if os.path.exists(CACHE_FILE) and not force_download:
        print(f"📂 Memuat data dari cache: {CACHE_FILE}")
        df = pd.read_csv(CACHE_FILE, index_col=0, parse_dates=True)
    else:
        print(f"📥 Mengunduh data baru dari Yahoo Finance...")
        try:
            data = yf.download(TICKERS, start=START_DATE, end=END_DATE, auto_adjust=True)
            if 'Close' in data.columns:
                df = data['Close']
            elif 'Adj Close' in data.columns:
                df = data['Adj Close']
            else:
                df = data.xs('Close', level=1, axis=1) if 'Close' in data.columns.get_level_values(1) else data
            
            if not os.path.exists(DATA_DIR):
                os.makedirs(DATA_DIR)
            df.to_csv(CACHE_FILE)
            print(f"💾 Data disimpan ke cache: {CACHE_FILE}")
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

    # --- 2. DATA CLEANING & RETURNS ---
    df = df.ffill()  # Isi data kosong
    returns = df.pct_change().dropna()  # Hitung daily returns
    
    print(f"✅ Data Siap! Dimensi Returns: {returns.shape}")
    return returns

if __name__ == "__main__":
    df_returns = load_stock_data()
    print("\n--- Contoh 5 Baris Data Returns ---")
    print(df_returns.head())