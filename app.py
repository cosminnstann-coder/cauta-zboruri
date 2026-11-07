import streamlit as st

st.set_page_config(page_title="Căutare Zboruri & Hoteluri", page_icon="✈️", layout="centered")

st.title("✈️ 🏨 Căutare Zboruri și Cazare Ieftină")

# Formular de căutare
col1, col2 = st.columns(2)
with col1:
    origine = st.text_input("Oraș Plecare (ex: OTP)", value="OTP").upper()
with col2:
    destinatie = st.text_input("Oraș Sosire (ex: BCN)", value="BCN").upper()

data_plecare = st.date_input("Data Plecare")
buget_max = st.number_input("Buget Maxim (€)", min_value=10, value=200)

if st.button("🔎 Caută Oferte"):
    with st.spinner("Se caută ofertele..."):
        st.success("Căutare finalizată!")
        st.metric(label="Zbor estimat (dus-întors)", value="45 €", delta="Optim")
        st.metric(label="Cazare medie / noapte", value="30 €", delta="Top Buget")
        st.info(f"Căutare salvată pentru ruta {origine} ➔ {destinatie} din {data_plecare}.")
