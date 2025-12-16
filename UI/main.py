import streamlit as st
import LogIn_WeatherApp.login_form as login_form
import weather

st.set_page_config(
    page_title="Weather App Login",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "login_from" not in st.session_state:
    st.session_state["login_from"] = False

if st.session_state["login_from"]:
    weather.weather_app()
    login_form.logout_button()
    
else:
    login_form.login_form()
