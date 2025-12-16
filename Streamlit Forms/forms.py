import streamlit as st
import json
with st.form(key='user_info_form'):
    user_name = st.text_input("Enter your name:")
    user_age = st.slider("Select You Age : ", 0, 120, 25)
    user_email = st.text_input("Enter your email address:")
    user_Address = st.text_area("Enter your address:")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        err_msg = ""
        if not user_name:
            err_msg += "Name cannot be empty. "
        if user_age < 0 or user_age > 120:
            err_msg += "Age must be between 0 and 120. "
        if not user_email:
            err_msg += "Email cannot be empty. "
        if not user_Address:
            err_msg += "Address cannot be empty. "
        if err_msg:
            st.error(err_msg)
        else:
            st.success(f"Name: {user_name}, Age: {user_age}, Email: {user_email}, Address: {user_Address}")

            user_data = {
                "name": user_name,
                "age": user_age,
                "email": user_email,
                "address": user_Address
            }
            with open('user_data.json', 'a') as f:
                json.dump(user_data, f,indent=4)
  # Add newline for separation
