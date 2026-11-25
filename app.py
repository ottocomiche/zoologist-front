import streamlit as st

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
