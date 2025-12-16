# 1. Make a chat bot like UI. Input a message from user and reply it back, but
# display the reply using st.write_stream(). Use delay to show chatlike effect.

import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

def stream_string_generator(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)

with st.sidebar:
    if st.title("Vision Chatbot"):
        st.session_state.page = "navigation"
    if st.button("Home", use_container_width= True):
        st.session_state.page = "home"
    if st.button("Register", use_container_width= True):
        st.session_state.page = "Register"
    if st.button("Login", use_container_width= True):
        st.session_state.page = "Login"

st.chat_input("Type your message here...", key="input")
if st.session_state.page == "home":
    st.title("Welcome to Vision Chatbot")
    st.write("This is the home page of the Vision Chatbot application.")
    st.write("Use the sidebar to navigate through different sections.")
elif st.session_state.page == "Register":
    st.title("Register Page")
    st.write("This is the Register page of the Vision Chatbot application.")
    st.write("Use the sidebar to navigate through different sections.")
elif st.session_state.page == "Login":
    st.title("Login Page")
    st.write("This is the Login page of the Vision Chatbot application.")
    st.write("Use the sidebar to navigate through different sections.")
else:
    st.title("Navigation Page")
    st.write("This is the Navigation page of the Vision Chatbot application.")
    st.write("Use the sidebar to navigate through different sections.")

