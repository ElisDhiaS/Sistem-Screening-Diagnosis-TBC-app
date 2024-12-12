import streamlit as st
import numpy as np
import pickle
from fpdf import FPDF
import base64
import os

def load_model():
    model_path = r"E:\Phoebe Intelligence\model_terbaik.pkl"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model


# Function to create PDF
def create_pdf(nama, usia, jenis_kelamin, hasil_prediksi):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Hasil Prediksi Kesehatan - TBC", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nama: {nama}", ln=True)
    pdf.cell(200, 10, txt=f"Usia: {usia}", ln=True)
    pdf.cell(200, 10, txt=f"Jenis Kelamin: {jenis_kelamin}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Hasil Prediksi: {hasil_prediksi}", ln=True)
    pdf.ln(10)
    
    if hasil_prediksi == "Suspek Positif TBC":
        pdf.multi_cell(0, 10, txt=(
            "Hasil prediksi menunjukkan bahwa Anda kemungkinan besar terindikasi positif TBC.\n"
            "Disarankan untuk segera melakukan pengobatan ke dokter untuk mendapatkan perawatan medis yang tepat.\n\n"
            "Langkah-langkah yang dapat Anda lakukan:\n"
            "1. KUNJUNGI DOKTER : Segera periksakan diri ke fasilitas kesehatan untuk konfirmasi diagnosis dan mendapatkan resep obat.\n"
            "2. PENGOBATAN : Jika terdiagnosis TBC, Anda akan diberikan obat anti-TB (seperti Isoniazid dan Rifampisin) selama 6-12 bulan. Pastikan untuk mengikuti semua anjuran dokter.\n"
            "3. KEPATUHAN : Jangan hentikan pengobatan sebelum waktunya untuk menghindari resistensi obat.\n"
            "4. PENCEGAHAN PENULARAN : Hindari kontak dekat dengan orang lain dan gunakan masker selama masa pengobatan.\n"
            "5. PERAWATAN DIRI : Jaga kebersihan, istirahat cukup, dan konsumsi makanan bergizi untuk mendukung sistem imun.\n\n"
            "Ingat, TBC dapat disembuhkan dengan pengobatan yang tepat dan disiplin.")
        )
    else:
        pdf.multi_cell(0, 10, txt=(
            "Hasil prediksi menunjukkan bahwa Anda kemungkinan besar tidak terindikasi TBC.\n"
            "Namun, jika Anda tetap merasakan gejala yang mengkhawatirkan atau berkepanjangan, "
            "disarankan untuk tetap berkonsultasi dengan dokter untuk memastikan kondisi kesehatan Anda.\n\n"
            "Tetap jaga kesehatan dengan:\n"
            "1. POLA HIDUP SEHAT : Makan makanan bergizi dan seimbang, Lakukan olahraga secara teratur.\n"
            "2. HINDARI FAKTOR RISIKO : Jauhi merokok dan paparan polusi udara.\n"
            "3. KEBERSIHAN DIRI DAN LINGKUNGAN : Jaga kebersihan diri dan lingkungan untuk mencegah penyakit menular.\n"
            "4. PEMERIKSAAN KESEHATAN BERKALA : Lakukan pemeriksaan kesehatan secara rutin untuk deteksi dini penyakit."
        ))

    return pdf

# User input function
def get_user_input():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .main-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            margin: auto;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .header img {
            width: 150px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .header h1 {
            margin-top: 20px;
            color: #007bff;
        }
        .header p {
            font-size: 1.2em;
            color: #555;
            margin-top: -10px;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            margin-top: 20px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .expander-header {
            font-weight: bold;
            font-size: 1.1em;
        }
        .info-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            font-size: 3em;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9em;
            color: #555555;
        }
        .question {
            background-color: #e0f7fa;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .answer {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
            list-style: none;
            padding-left: 20px;
        }
        .answer li {
            margin-bottom: 5px;
        }
        .pamphlet {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 20px;
        }
        .pamphlet img {
            width: 80%;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .team-member {
            text-align: center;
            margin-top: 20px;
        }
        .team-member img {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
            margin-bottom: 10px;
        }
        .team-member h3 {
            margin: 5px 0;
        }
        .team-member p {
            color: #666;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="header">
            <h1>Sistem Screening Kesehatan TBC</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.expander("Masukkan Data Diri Anda"):
        nama = st.text_input("Nama")
        usia = st.number_input("Usia", min_value=0, max_value=120, step=1)
        jenis_kelamin = st.selectbox("Jenis Kelamin", ('Laki-laki', 'Perempuan'))

    with st.expander("Masukkan gejala TBC"):
        Batuk = st.selectbox("Batuk", ('Tidak batuk', 'Batuk biasa', 'Batuk berdahak', 'Batuk lama', 'Batuk berdarah'))
        Sesaknafas = st.selectbox("Sesak nafas", ('Tidak sesak', 'Sedang', 'Berat dan Berulang'))
        Nyeridada = st.selectbox("Nyeri dada", ('Tidak nyeri', 'Jarang', 'Sering'))
        Demampadasoreataumalamhari = st.selectbox("Demam pada sore atau malam hari", ('Tidak', 'Kadang-kadang demam', 'Demam agak panas', 'Panas sekali'))
        Penurunannafsumakan = st.selectbox("Penurunan nafsu makan", ('Tidak turun', 'Turun'))
        Badanlemah = st.selectbox("Badan lemah", ('Tidak lemah', 'Lemah'))

    # Convert descriptive input to numeric values
    def convert_input(input_str):
        mapping = {
            'Tidak batuk': 0, 'Batuk biasa': 1, 'Batuk berdahak': 2, 'Batuk lama': 3, 'Batuk berdarah': 4,
            'Tidak sesak': 0, 'Sedang': 1, 'Berat dan Berulang': 2,
            'Tidak nyeri': 0, 'Jarang': 1, 'Sering': 2,
            'Tidak': 0, 'Kadang-kadang demam': 1, 'Demam agak panas': 2, 'Panas sekali': 3,
            'Tidak turun': 0, 'Turun': 1,
            'Tidak lemah': 0, 'Lemah': 1
        }
        return mapping[input_str]

    user_input = np.array([
        convert_input(Batuk),
        convert_input(Sesaknafas),
        convert_input(Nyeridada),
        convert_input(Demampadasoreataumalamhari),
        convert_input(Penurunannafsumakan),
        convert_input(Badanlemah)
    ]).reshape(1, -1)

    return nama, usia, jenis_kelamin, user_input

# Main function
def main():
    st.sidebar.title("Menu")
    page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Screening TBC"])

    if page == "Home":
        st.markdown('<div class="info-container">', unsafe_allow_html=True)

        st.image("Screening_TBC.png")

        st.markdown('<div class="header"><h2>Informasi Lengkap Tentang TBC</h2></div>', unsafe_allow_html=True)

        questions_and_answers = [
            ("Apa itu Tuberkulosis (TBC)?",
             ["Tuberkulosis (TBC) adalah penyakit menular yang disebabkan oleh bakteri Mycobacterium tuberculosis.",
              "Penyakit ini dapat menyerang berbagai bagian tubuh, tetapi paling umum menyerang paru-paru. TBC dapat menyebar melalui udara ketika seseorang yang terinfeksi batuk, bersin, atau berbicara, dan orang lain menghirup droplet yang mengandung kuman tersebut."]),

            ("Apa saja gejala umum TBC?",
             ["Batuk yang berlangsung lama (3 minggu atau lebih), sering disertai dengan dahak atau darah.",
              "Nyeri dada saat bernapas atau batuk.",
              "Kelelahan dan hilang nafsu makan",
              "Penurunan berat badan yang tidak dapat dijelaskan",
              "Demam dan menggigil",
              "Berkeringat di malam hari"]),
            
            ("Siapa yang paling berisiko TBC?",
             ["Anak-anak, terutama belum divaksinasi",
              "Penyintas HIV/AIDS yang memiliki sistem imun yang lemah",
              "Orang lanjut usia, yang mungkin memiliki kesehatan yang lebih rentan",
              "Perokok, yang memiliki risiko lebih tinggi untuk infeksi paru-paru",
              "Orang dengan diabetes atau kondisi medis lainnya yang melemahkan sistem imun",
              "Individu yang memiliki kontak dekat dengan pasien TBC aktif"]),
                        
            ("Bagaimana cara penularan TBC?",
             ["TBC menyebar melalui udara. Ketika seseorang yang terinfeksi batuk atau bersin, kuman TB dapat tersebar dalam bentuk droplet kecil yang dapat dihirup oleh orang lain.",
              "Satu kali batuk bisa mengeluarkan sekitar 3000 droplet, sedangkan sekali bersin bisa mengeluarkan antara 4500 hingga 1 juta droplet."]),

            ("Bagaimana cara mencegah TBC?",
             ["Beberapa langkah untuk menghindari TBC antara lain:",
              "Vaksinasi BCG (Bacillus Calmette-Guerin) : Vaksin ini diberikan kepada anak-anak untuk membantu melindungi mereka dari TBC",
              "Menghindari kontak dekat, Jauhi orang yang terinfeksi TB aktif",
              "Menggunakan masker, Saat berada di tempat yang ramai atau berisiko tinggi",
              "Menjaga kebersihan, Selalu cuci tangan dan jaga kebersihan lingkungan"]),

            ("Bagaimana pengobatan TBC?",
             ["Pengobatan TBC melibatkan kombinasi antibiotik yang harus diminum secara teratur selama 6 bulan atau lebih.",
              "Obat-obatan ini termasuk Isoniazid, Rifampisin, Pirazinamid, dan Etambutol.",
              "Penting untuk menyelesaikan seluruh regimen pengobatan untuk mencegah resistensi bakteri."]),

            ("Di mana saya bisa mendapatkan perawatan untuk TBC?",
             ["Puskesmas setempat",
              "Rumah sakit umum",
              "Klinik yang menyediakan layanan kesehatan"])
        ]

        for q, a in questions_and_answers:
            st.markdown(f'<div class="question">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<ul class="answer">{" ".join(f"<li>{item}</li>" for item in a)}</ul>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="pamphlet">
                <h2>Pamflet Informasi TBC</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Menampilkan pamflet menggunakan st.image
        st.image('TUBERCULOSIS.jpeg') 

        st.markdown(
            """
            <div class="footer">
                <p>&copy; 2024 Sistem Screening Kesehatan - TBC. All Rights Reserved.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # Main function
    if page == "Screening TBC":
        
        model = load_model()
        nama, usia, jenis_kelamin, user_input = get_user_input()

        if st.button("Prediksi"):
            hasil = model.predict(user_input)[0]
            hasil_prediksi = "Suspek Positif TBC" if hasil == 1 else "Suspek Negatif TBC"

            result_class = "positive-result" if hasil_prediksi == "Suspek Positif TBC" else "negative-result"
            
            st.markdown(
                f"""
                <div style="border: 2px solid #007bff; padding: 20px; border-radius: 10px; margin-top: 20px;">
                    <h3>Hasil Prediksi</h3>
                    <p><strong>Nama:</strong> {nama}</p>
                    <p><strong>Usia:</strong> {usia}</p>
                    <p><strong>Jenis Kelamin:</strong> {jenis_kelamin}</p>
                    <p><strong>Hasil Prediksi:</strong> {hasil_prediksi}</p>
                </div>
                """, unsafe_allow_html=True)

            pdf = create_pdf(nama, usia, jenis_kelamin, hasil_prediksi)
            pdf_output = f"{nama}_hasil_prediksi_TBC.pdf"
            pdf.output(pdf_output)
            
            with open(pdf_output, "rb") as file:
                pdf_data = file.read()
            
            b64_pdf = base64.b64encode(pdf_data).decode('utf-8')
            pdf_link = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="{pdf_output}">Download Hasil Prediksi</a>'
            st.markdown(pdf_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
