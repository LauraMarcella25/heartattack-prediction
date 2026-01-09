import streamlit as st
import pickle
import numpy as np
from pathlib import Path

# ================= CONFIG =================
st.set_page_config(
    page_title="HeartSense",
    page_icon="❤️",
    layout="wide"
)

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"
st.markdown("""
<style>
/* WARNA BACKGROUND GLOBAL */
body {
    background-color: #EEF1FF;
}

/* BALIK KE STREAMLIT DEFAULT, TAPI RAPI */
.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
    padding-bottom: 2rem;
}

/* RESPONSIVE PADDING (LAYAR KECIL) */
@media (max-width: 900px) {
    .block-container {
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
}

/* HERO */
.hero {
    background-color: #EEF1FF;
    padding: 60px 0;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    color: #1f2937;
}

.hero p {
    font-size: 17px;
    color: #4b5563;
}

/* BUTTON STREAMLIT STYLE (BIRU) */
.stButton > button {
    background-color: #3B5BDB !important;
    color: white !important;
    padding: 10px 26px;
    border-radius: 8px;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background-color: #2f4acb !important;
}

/* CARD */
.card {
    background: white;
    padding: 22px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 6px 16px rgba(0,0,0,0.06);
}

/* SECTION */
.section {
    padding: 60px 0;
    background: white;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 32px;
}

.soft {
    background-color: #F5F7FF;
    padding: 60px 0;
}
</style>
""", unsafe_allow_html=True)



# ================= SESSION =================
if "page" not in st.session_state:
    st.session_state.page = "home"

# ================= LOAD MODEL =================
# Pastikan file ModelHeartAttack.pkl ada di folder yang sama
with open(BASE_DIR / "ModelHeartAttack.pkl", "rb") as f:
    model = pickle.load(f)

# ================= HOME =================
def home_page():
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    c1, c2 = st.columns([1.3,1])

    with c1:
        st.markdown("""
        <h1>Prediksi Risiko Jantung<br>Anda dengan Teknologi AI</h1>
        <p>Analisis cepat, akurat, dan mudah dipahami<br>
        berdasarkan data kesehatan anda</p>
        """, unsafe_allow_html=True)

        if st.button("Cek Risiko Sekarang"):
            st.session_state.page = "predict"
            st.rerun()

        c3, c4 = st.columns(2)
        with c3:
            st.markdown("""
            <div class="card">
            <b>AI Risk Prediction</b>
            <p>Model machine learning untuk prediksi risiko jantung</p>
            </div>
            """, unsafe_allow_html=True)
        with c4:
            st.markdown("""
            <div class="card">
            <b>Personal Health Insight</b>
            <p>Analisis personal untuk keputusan kesehatan</p>
            </div>
            """, unsafe_allow_html=True)

    with c2:
        # Pastikan file heart.png ada di folder assets
        st.image(str(ASSETS / "heart.png"), width=420)

    st.markdown('</div>', unsafe_allow_html=True)

    # HOW IT WORKS
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
    w1, w2, w3 = st.columns(3)
    with w1:
        st.markdown("**1️⃣ Masukan data anda**<br>Usia, tekanan darah, dll", unsafe_allow_html=True)
    with w2:
        st.markdown("**2️⃣ AI menganalisis**<br>Model memproses data", unsafe_allow_html=True)
    with w3:
        st.markdown("**3️⃣ Lihat skor risiko**<br>Hasil prediksi", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # VISI MISI
    st.markdown('<div class="section soft">', unsafe_allow_html=True)
    v1, v2 = st.columns(2)
    with v1:
        st.markdown("### Visi\nMemudahkan skrining risiko jantung")
    with v2:
        st.markdown("""
        ### Misi
        1. Prediksi risiko akurat  
        2. Edukasi pencegahan  
        3. Akses skrining awal
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # STORY
    st.markdown('<div class="section">', unsafe_allow_html=True)
    s1, s2 = st.columns([1.3,1])
    with s1:
        st.markdown("""
        ### Our Story
        HeartSense hadir untuk membantu deteksi dini risiko jantung
        menggunakan AI agar lebih mudah diakses dan dipahami.
        """)
    with s2:
        # Pastikan file doctor.png ada di folder assets
        st.image(str(ASSETS / "doctor.png"), width=260)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= PREDICT (INPUT DATA) =================
def predict_page():
    st.markdown("## 🩺 Masukkan Data Kesehatan Anda")

    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.number_input("Usia", 1, 120)
        sex = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        cp = st.selectbox("Tipe Nyeri Dada", [0,1,2,3])
        trestbps = st.number_input("Tekanan Darah", 80, 200)
        chol = st.number_input("Kolesterol", 100, 600)
        fbs = st.number_input("Gula Darah", 120, 1000)

    with c2:
        restecg = st.selectbox("ECG", [0,1,2])
        thalach = st.number_input("Detak Maks", 60, 220)
        exang = st.selectbox("Nyeri saat Olahraga", [tidak,iya])
        oldpeak = st.number_input("Oldpeak", 0.0, 6.0)
        slope = st.selectbox("Slope", [0,1,2])
        ca = st.selectbox("Pembuluh", [0,1,2,3,4])

    with c3:
        thal = st.selectbox("Thal", [0,1,2,3])
        bmi = st.number_input("BMI", 10.0, 50.0)
        smoking = st.selectbox("Apakah anda Merokok?", [tidak,iya])
        alcohol = st.selectbox("Apakah anda Alkohol?", [tidak,iya])
        exercise = st.selectbox("Apakah anda Olahraga?", [tidak,iya])
        diabetes = st.selectbox("Apakah anda Diabetes?", [tidak,iya])

    if st.button("Analisis Risiko"):
        # Simpan input data ke session state agar bisa dibaca di halaman result
        st.session_state.input_data = np.array([[age,1 if sex=="Laki-laki" else 0,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,bmi,smoking,alcohol,exercise,diabetes]])
        st.session_state.page = "result"
        st.rerun()

# ================= RESULT (HASIL PREDIKSI) =================
def result_page():
    st.markdown("## 🧠 Hasil Prediksi Risiko Jantung")
    
    # Cek apakah data input ada
    if "input_data" not in st.session_state:
        st.error("Data tidak ditemukan. Silakan kembali ke halaman Home.")
        if st.button("Kembali ke Home"):
            st.session_state.page = "home"
            st.rerun()
        return

    # AMBIL DATA DARI SESSION DAN PREDIKSI
    input_data = st.session_state.input_data
    
    try:
        # Prediksi menggunakan model yang sudah di-load
        prediction = model.predict(input_data)[0]           # 0 atau 1
        prediction_proba = model.predict_proba(input_data)[0][1] # Probabilitas (misal 0.85)
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses data: {e}")
        return

    model_accuracy = 0.92  # Akurasi statis (sesuai kode awal)

    # KONDISI RISIKO
    if prediction == 0:
        st.success("✅ **Risiko Rendah**")
        st.success("Hasil ini buka merupakan diagnosis medis profesional. Berdasarkan analisis data yang anda masukan , model AI kami mendeteksi indikasi resiko rendah, Tetap jaga kesehatan dan lakukan pemeriksaan rutin.")
    else:
        st.error("⚠️ **Risiko Tinggi**")
        st.error("Hasil ini buka merupakan diagnosis medis profesional. Berdasarkan analisis data yang anda masukan , model AI kami mendeteksi indikasi yang memerlukan perhatian serius dan tindak lanjut segera")

    # TAMPILKAN PERSENTASE
    st.markdown(f"""
    ### 📊 Detail Prediksi
    - **Akurasi Model:** **{model_accuracy * 100:.0f}%**
    """)

    # PROGRESS BAR
    st.progress(float(prediction_proba))

    st.markdown("---")

    # TOMBOL KEMBALI KE HOME
    if st.button("⬅️ Kembali ke Home"):
        st.session_state.page = "home"
        st.rerun()

# ================= ROUTER =================
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "predict":
    predict_page()
elif st.session_state.page == "result":
    result_page()