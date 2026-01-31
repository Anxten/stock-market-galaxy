import os
import yfinance as yf
import pandas as pd
from src.config import TICKERS, START_DATE, END_DATE

# Lokasi penyimpanan cache
DATA_DIR = "data"
CACHE_FILE = os.path.join(DATA_DIR, "stock_prices.csv")

def load_stock_data(force_download=False):
    """
    Mengunduh data saham.
    Jika file cache ada, baca dari file. Jika tidak, download dari Yahoo Finance.
    Param:
        force_download (bool): Paksa download ulang meskipun cache ada.
    """
    # Cek apakah cache tersedia
    if os.path.exists(CACHE_FILE) and not force_download:
        print(f"📂 Memuat data dari cache: {CACHE_FILE}")
        # index_col=0 artinya kolom pertama (Date) dijadikan index
        df = pd.read_csv(CACHE_FILE, index_col=0, parse_dates=True)
        print(f"✅ Data dimuat! Dimensi: {df.shape}")
        return df

    # Jika tidak ada cache, download baru
    print(f"📥 Mengunduh data baru dari Yahoo Finance...")
    try:
        data = yf.download(TICKERS, start=START_DATE, end=END_DATE, auto_adjust=True)
        
        # Bersihkan struktur kolom
        if 'Close' in data.columns:
            data = data['Close']
        elif 'Adj Close' in data.columns:
            data = data['Adj Close']
        else:
            data = data.xs('Close', level=1, axis=1) if 'Close' in data.columns.get_level_values(1) else data

        # Simpan ke CSV (Caching)
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            
        data.to_csv(CACHE_FILE)
        print(f"💾 Data disimpan ke cache: {CACHE_FILE}")
        print(f"✅ Berhasil! Dimensi: {data.shape}")
        return data

    except Exception as e:
        print(f"❌ Error saat download: {e}")
        return None

if __name__ == "__main__":
    # Test 1: Download pertama kali (akan membuat file CSV)
    df = load_stock_data()
    
    # Test 2: Load kedua kali (harus baca dari cache, perhatikan log-nya)
    print("\n--- Test Caching ---")
    df_cache = load_stock_data()