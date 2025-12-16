import streamlit as st
import time
from dotenv import load_dotenv
import os
import def_gemini as dg
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("Gemini Chatbot")
st.sidebar.title("Gemini Chatbot")

prompt = st.chat_input("Type your message here...", key="input")
st.session_state.setdefault("messages", [])
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = dg.call_gemini(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

    

