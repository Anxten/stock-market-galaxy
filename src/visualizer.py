import plotly.express as px
from src.clustering import get_clustered_data

def create_galaxy_plot():
    """
    Membuat Plot 3D Interaktif dari data saham.
    Sumbu X, Y, Z adalah PC1, PC2, PC3.
    Warna adalah Cluster.
    """
    # Ambil Data yang sudah ada Cluster-nya
    df = get_clustered_data()
    if df is None:
        return None

    # Reset Index supaya Ticker jadi kolom biasa (untuk label)
    df_plot = df.reset_index()
    df_plot.columns = ['Ticker', 'PC1', 'PC2', 'PC3', 'Cluster']

    # Bikin 3D Scatter Plot
    fig = px.scatter_3d(
        df_plot,
        x='PC1',
        y='PC2',
        z='PC3',
        color='Cluster',
        hover_name='Ticker',  # Nama saham saat hover
        title='Stock Market Galaxy 🌌 (IHSG Bluechips)',
        labels={'Cluster': 'Kelompok'},
        opacity=0.9,
        size_max=10
    )

    # Background gelap ala luar angkasa
    fig.update_layout(
        template="plotly_dark",
        margin=dict(l=0, r=0, b=0, t=40)
    )
    
    return fig

if __name__ == "__main__":
    # Test script: Akan membuka browser/file HTML
    fig = create_galaxy_plot()
    if fig:
        fig.show()  # Membuka tab baru di browser