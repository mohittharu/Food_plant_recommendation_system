import streamlit as st
from main import predict

st.set_page_config(
    page_title="Food Crop Recommendation",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Food Plant Recommendation System")
st.write("Enter soil parameters below to predict the most suitable crop.")

# Input layout
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
    soil_ec = st.number_input("Soil EC", min_value=0.0, step=0.01)
    phosphorus = st.number_input("Phosphorus", min_value=0.0, step=0.1)

with col2:
    potassium = st.number_input("Potassium", min_value=0.0, step=0.1)
    tsp = st.number_input("TSP (Triple Super Phosphate)", min_value=0.0, step=0.1)
    mop = st.number_input("MOP (Muriate of Potash)", min_value=0.0, step=0.1)

if st.button("🔮 Predict"):
    try:
        # ⚠️ Make sure feature order matches training data
        input_data = [ph, soil_ec, phosphorus, potassium, tsp]

        prediction, confidence = predict(input_data)

        st.success(f"🌾 Recommended Crop: **{prediction}**")
        st.info(f"🔒 Confidence: **{round(confidence * 100, 2)} %")

    except Exception as e:
        st.error(f"⚠ Prediction Failed: {e}")
