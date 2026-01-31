import yfinance as yf
import pandas as pd
from src.config import TICKERS, START_DATE, END_DATE

def load_stock_data():
    """
    Mengunduh data saham dari Yahoo Finance.
    Mengembalikan DataFrame berisi harga 'Close' yang sudah disesuaikan (Adjusted).
    """
    print(f"📥 Mengunduh data untuk {len(TICKERS)} saham...")
    print(f"📅 Periode: {START_DATE} s/d {END_DATE}")
    
    try:
        # Download data saham dengan auto_adjust=True untuk harga yang sudah disesuaikan
        data = yf.download(TICKERS, start=START_DATE, end=END_DATE, auto_adjust=True)
        
        # Ekstrak kolom Close berdasarkan struktur data yang diterima
        if 'Close' in data.columns:
            data = data['Close']
        elif 'Adj Close' in data.columns:
            data = data['Adj Close']
        else:
            print("⚠️ Struktur kolom berbeda, mencoba akses level atas...")
            # Untuk multi-level columns (multiple tickers)
            data = data.xs('Close', level=1, axis=1) if 'Close' in data.columns.get_level_values(1) else data
            
    except Exception as e:
        print(f"❌ Error saat formatting data: {e}")
        return None

    if data.empty:
        print("❌ Gagal mengunduh data! Cek koneksi internet atau nama ticker.")
        return None
    
    print(f"✅ Berhasil! Dimensi data: {data.shape}")
    return data

if __name__ == "__main__":
    df = load_stock_data()
    if df is not None:
        print(df.head())