import streamlit as st
import requests
st.title("Zoologist front")

st.markdown("Enter the characteristics of a penguin to predict its species.")

island = st.selectbox(
    "Island",
    ["Biscoe", "Dream", "Torgersen"]
)

bill_length_mm = st.number_input(
    "Bill length (mm)",
    min_value=0.0,
    value=45.0,
    step=0.1
)

bill_depth_mm = st.number_input(
    "Bill depth (mm)",
    min_value=0.0,
    value=17.0,
    step=0.1
)

flipper_length_mm = st.number_input(
    "Flipper length (mm)",
    min_value=0,
    value=200
)

body_mass_g = st.number_input(
    "Body mass (g)",
    min_value=0,
    value=4000
)

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)
API_URL = f"{st.secrets['API_URL']}/predict"

params = {
    "island": island,
    "bill_length_mm": bill_length_mm,
    "bill_depth_mm": bill_depth_mm,
    "flipper_length_mm": flipper_length_mm,
    "body_mass_g": body_mass_g,
    "sex": sex
}
if st.button("Predict penguin species"):
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicted species: {prediction}")
    else:
        st.error(f"API error: {response.status_code}")
