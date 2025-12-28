import streamlit as st
import pandas as pd
import random
import os
from codecarbon import EmissionsTracker
from src.Algorithms import BellmanFord, FloydWarshall, Knapsack
from src.Main import get_easy_data, get_middle_data, get_hard_data

# Sayfa tasarımı
st.set_page_config(page_title="Algoritma Enerji Analizi", layout="wide")

st.title("⚡ Algoritma Enerji Emisyon Ölçümü")
st.markdown("""
Bu uygulama, farklı algoritmaların işlem karmaşıklığına göre karbon ayak izini ölçer. 
Veriler **CodeCarbon** kütüphanesi kullanılarak gerçek zamanlı hesaplanır.
""")

# --- Yan Panel (Sidebar) ---
st.sidebar.header("Deney Parametreleri")

# Algoritma seçimi
selected_algo = st.sidebar.selectbox(
    "Test Edilecek Algoritma",
    ["Bellman-Ford", "Floyd-Warshall", "Knapsack"]
)

# Zorluk seviyesi seçimi
difficulty = st.sidebar.select_slider(
    "Veri Seti Zorluğu",
    options=["Kolay", "Orta", "Zor"]
)

# Tekrar sayısı (Enerji ölçümünün anlamlı olması için yüksek olmalıdır)
iterations = st.sidebar.number_input("Tekrar Sayısı (Repeat)", min_value=1, value=1000, step=500)

# --- Veri Hazırlığı ---
# Main.py içerisindeki hazır fonksiyonları kullanıyoruz
if difficulty == "Kolay":
    V, edges, matrix, weights, values, capacity = get_easy_data()
elif difficulty == "Orta":
    V, edges, matrix, weights, values, capacity = get_middle_data()
else:
    V, edges, matrix, weights, values, capacity = get_hard_data()


# --- Ölçüm Fonksiyonu ---
def measure_energy():
    tracker = EmissionsTracker(
        project_name=f"{selected_algo}_{difficulty}"
    )

    with st.spinner(f'{selected_algo} çalıştırılıyor, lütfen bekleyin...'):
        tracker.start()

        # Algoritma seçimine göre sınıfın örneğini oluştur ve çalıştır
        if selected_algo == "Bellman-Ford":
            # BellmanFord(V, source, edges)
            bf = BellmanFord(V, 0, edges)
            for _ in range(iterations):
                bf.BellmanFordAlgorithm()

        elif selected_algo == "Floyd-Warshall":
            # FloydWarshall(distance_matrix)
            fw = FloydWarshall(matrix)
            for _ in range(iterations):
                fw.FloyWarshall()

        elif selected_algo == "Knapsack":
            # Knapsack(weights, values, capacity)
            ks = Knapsack(weights, values, capacity)
            for _ in range(iterations):
                ks.Knapsack()

        emissions = tracker.stop()
    return emissions


# --- Arayüz İçeriği ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Veri Seti Özellikleri")
    stats = {
        "Parametre": ["Düğüm Sayısı (V)", "Kenar/Öğe Sayısı", "Zorluk"],
        "Değer": [V, len(edges) if selected_algo != "Knapsack" else len(weights), difficulty]
    }
    st.table(pd.DataFrame(stats))

    if st.button("Ölçümü Başlat", type="primary"):
        carbon_result = measure_energy()
        st.session_state['result'] = carbon_result

with col2:
    st.subheader("Ölçüm Sonuçları")
    if 'result' in st.session_state:
        res = st.session_state['result']

        # Metrik kutuları
        m1, m2 = st.columns(2)
        m1.metric("CO2 Emisyonu (kg)", f"{res:.10f}")
        m2.metric("Tekrar Sayısı", iterations)

        st.success("Analiz başarıyla tamamlandı. Sonuçlar 'emissions.csv' dosyasına eklenmiştir.")

        # Geçmiş Verileri Göster (Opsiyonel)
        if os.path.exists("emissions.csv"):
            st.markdown("### Son Ölçümler")
            df_history = pd.read_csv("emissions.csv")
            st.dataframe(df_history.tail(5))

# --- Algoritma Bilgisi ---
st.divider()
st.info(
    f"**Seçilen Algoritma Hakkında:** {selected_algo} algoritması {difficulty} zorluk seviyesinde toplam {iterations} kez koşturularak enerji tüketimi hesaplanmaktadır.")