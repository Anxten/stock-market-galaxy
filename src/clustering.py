from sklearn.cluster import KMeans
from src.pca_engine import get_pca_data

def get_clustered_data(n_clusters=4):
    """
    Mengambil data PCA dan melakukan pengelompokan (Clustering) menggunakan K-Means.
    """
    # Ambil Data Koordinat Galaxy (PCA)
    pca_df = get_pca_data()
    if pca_df is None:
        return None
    
    # Jalankan K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(pca_df)
    
    # Simpan Label Cluster ke DataFrame
    pca_df['Cluster'] = kmeans.labels_
    pca_df['Cluster'] = pca_df['Cluster'].astype(str)  # Konversi ke string untuk kategori
    
    print(f"✅ Clustering Selesai! Ditemukan {n_clusters} kelompok saham.")
    return pca_df

if __name__ == "__main__":
    df = get_clustered_data()
    print("\n--- Hasil Pengelompokan Saham ---")
    # Tampilkan saham per cluster
    for cluster_id in sorted(df['Cluster'].unique()):
        print(f"\n📁 Cluster {cluster_id}:")
        members = df[df['Cluster'] == cluster_id].index.tolist()
        print(", ".join(members))