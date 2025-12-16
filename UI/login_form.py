import streamlit as st
import pandas as pd

def login_form():
    st.title("Login Form with PandasQL")
    
    if "logout_message" in st.session_state:
        st.success(st.session_state["logout_message"])
        del st.session_state["logout_message"]

    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")


    if st.button("Login"):
        if username == "23uam015" and password == "dkte123":
            st.success("Login successful!")
            st.session_state["login_from"] = True
            st.balloons()
            st.rerun()
        else:
            st.error("Invalid username or password.")

def logout_button(): 
    logout = st.button("Logout") 
    if logout:
        st.session_state["logout_message"] = "Thank you for using our app. You have been logged out successfully!"
        st.session_state["login_from"] = False 
        st.rerun()