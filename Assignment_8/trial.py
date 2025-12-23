import streamlit as st
import gemini
import groq
import local_llm
import time
st.set_page_config(
    page_title="Vision ChatBot",
    layout="centered",
    page_icon="🤖"
)
def stream_string_generator(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)

if "page" not in st.session_state:
    st.session_state.page = "gemini"
    st.header("Welcome to Vision ChatBot! Choose a chatbot from the sidebar.")
    st.write("This application allows you to interact with three different chatbots: Gemini, Groq, and a Local LLM. Use the sidebar to select which chatbot you'd like to converse with.")

if "messages_groq" not in st.session_state:
    st.session_state.messages_groq = []

with st.sidebar:
    st.title("Vision Chatbot")
# -------- Main Page --------
    prompt = st.chat_input("Type your message here...")

    if prompt:
        st.session_state.messages_groq.append({
            "role": "user",
            "content": prompt
        })
        response = groq.groq_call(prompt)
        st.session_state.messages_groq.append({
            "role": "assistant",
            "content": response
        })

    for msg in st.session_state.messages_groq:
        st.chat_message(msg["role"]).write(msg["content"])