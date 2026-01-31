import pandas as pd
from sklearn.decomposition import PCA
from src.loader import load_stock_data

def get_pca_data(n_components=3):
    """
    Mengubah data returns saham menjadi koordinat PCA (X, Y, Z).
    """
    # Load Data Returns
    returns = load_stock_data()
    if returns is None:
        return None
    
    # Transpose Data - kelompokkan SAHAM (kolom), bukan HARI (baris)
    X = returns.T
    
    # Jalankan PCA
    pca = PCA(n_components=n_components)
    coords = pca.fit_transform(X)
    
    # Rapikan hasil jadi DataFrame
    columns = [f'PC{i+1}' for i in range(n_components)]
    pca_df = pd.DataFrame(coords, columns=columns, index=X.index)
    
    # Explained variance ratio
    explained_variance = pca.explained_variance_ratio_.sum()
    
    print(f"✅ PCA Selesai! Dimensi Galaxy: {pca_df.shape}")
    print(f"📊 Informasi Data yang tersimpan: {explained_variance:.2%}")
    
    return pca_df

if __name__ == "__main__":
    df_pca = get_pca_data()
    print("\n--- Koordinat Galaxy Saham (3 Dimensi) ---")
    print(df_pca)