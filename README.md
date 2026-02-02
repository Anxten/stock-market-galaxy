# 🌌 Stock Market Galaxy (IHSG Edition)

**Stock Market Galaxy** adalah proyek *Unsupervised Machine Learning* yang memvisualisasikan pasar saham Indonesia (IHSG) dalam bentuk galaksi 3 dimensi.

Proyek ini menggunakan **Principal Component Analysis (PCA)** untuk mereduksi dimensi data, dan **K-Means Clustering** untuk mengelompokkan saham berdasarkan pola pergerakan harganya.

## 🧠 Core Tech Stack

* **Linear Algebra:** PCA (Eigen-decomposition) untuk Dimensionality Reduction.
* **Machine Learning:** K-Means Clustering.
* **Data:** `yfinance` (Yahoo Finance API) - Auto caching system.
* **Visualization:** Plotly 3D Interactive.
* **Web App:** Streamlit.

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Anxten/stock-market-galaxy.git
cd stock-market-galaxy
```

### 2. Setup Environment

```bash
# Buat Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install Dependencies
pip install -r requirements.txt
```

### 3. Run Application

```bash
streamlit run app.py
```

## 📊 Insight & Discovery

Dari analisis saham LQ45 (2023-2025), AI menemukan pola menarik:

* **GOTO** terdeteksi sebagai outlier (terpisah dari cluster utama) karena volatilitas tinggi.
* **ADRO & PTBA** (Sektor Energi) dikelompokkan dalam satu cluster yang sama secara otomatis.
* **Banking (BBCA, BBRI)** membentuk cluster "Market Movers" yang stabil.

---

*Created by Allan Bendatu - Informatics Student*