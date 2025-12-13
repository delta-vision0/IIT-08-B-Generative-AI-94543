import streamlit as st

name = st.text_input("Enter your name:")
message = st.text_area("Enter your message:" , height=100)
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "csv"])

model = st.selectbox("Select Model", ["Gemini Pro", "Gemini 1.5", "Gemini 1.0"])

if name:
    st.write(f"Hello, {name}!")

st.markdown("**This is Bold Text** and *this is Italic Text*.")

import pandas as pd
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)