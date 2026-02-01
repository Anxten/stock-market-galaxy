import streamlit as st
import plotly.express as px
from src.visualizer import create_galaxy_plot
from src.loader import load_stock_data

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="Stock Market Galaxy",
    page_icon="🌌",
    layout="wide"
)

# 2. Judul dan Deskripsi
st.title("🌌 Stock Market Galaxy: IHSG Bluechips")
st.markdown("""
**Selamat datang di Peta 3D Pasar Saham Indonesia!**
Visualisasi ini menggunakan **Principal Component Analysis (PCA)** untuk mereduksi data pergerakan harga saham
menjadi 3 dimensi, lalu mengelompokkannya menggunakan **K-Means Clustering**.

* **Titik yang berdekatan:** Saham yang pergerakan harganya mirip (satu sektor/karakter).
* **Warna yang sama:** Saham yang dikelompokkan dalam satu cluster oleh AI.
""")

# 3. Sidebar (Panel Kiri)
with st.sidebar:
    st.header("⚙️ Control Panel")
    st.info("Aplikasi ini menganalisis data harian saham LQ45 terpilih (2 Tahun Terakhir).")
    
    # Tombol Refresh Data
    if st.button("🔄 Reload Data from Yahoo Finance"):
        st.cache_data.clear()
        load_stock_data(force_download=True)
        st.success("Data berhasil diperbarui!")

# 4. Tampilkan Grafik Galaxy
st.subheader("Interactive 3D Clustering")

# Loading spinner untuk UX yang lebih baik
with st.spinner('Loading galaxy visualization...'):
    try:
        fig = create_galaxy_plot()
        if fig:
            # Tampilkan grafik Plotly di dalam Streamlit
            st.plotly_chart(fig, use_container_width=True, height=700)
        else:
            st.error("Gagal memuat visualisasi. Cek koneksi internet.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

# 5. Penjelasan Analisis (Footer)
st.divider()
st.markdown("### 🔍 Insight")
st.markdown("""
- **Cluster Terpisah:** Jika ada saham yang menyendiri jauh dari kerumunan, artinya saham tersebut memiliki anomali atau volatilitas unik (contoh: Saham Tech vs Banking).
- **Sumbu PCA:** Sumbu X, Y, Z tidak memiliki satuan harga, melainkan representasi varians data (Matematika Aljabar Linier).
""")

st.caption("Created by Allan Bendatu - Informatics Student | Powered by Python, Scikit-Learn, & Streamlit")