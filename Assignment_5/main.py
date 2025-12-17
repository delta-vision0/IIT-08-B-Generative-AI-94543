import streamlit as st
import gemini
import groq
import local_llm
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
if "messages_gemini" not in st.session_state:
    st.session_state.messages_gemini = []

if "messages_groq" not in st.session_state:
    st.session_state.messages_groq = []

if "messages_local" not in st.session_state:
    st.session_state.messages_local = []


with st.sidebar:
    st.title("Vision Chatbot")

    if st.button("Gemini Chatbot", use_container_width=True):
        st.session_state.page = "gemini"

    if st.button("Groq Chatbot", use_container_width=True):
        st.session_state.page = "groq"

    if st.button("Local Chatbot", use_container_width=True):
        st.session_state.page = "local"

# -------- Main Page --------
if st.session_state.page == "gemini":
    st.title("Gemini ChatBot")
    prompt = st.chat_input("Type your message here...")

    if prompt:
        st.session_state.messages_gemini.append({
            "role": "user",
            "content": prompt
        })
        response = gemini.gemini_call(prompt)
        st.session_state.messages_gemini.append({
            "role": "assistant",
            "content": response
        })

    for msg in st.session_state.messages_gemini:
        st.chat_message(msg["role"]).write(msg["content"])

if st.session_state.page == "groq":
    st.title("Groq Chatbot")
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

if st.session_state.page == "local":
    st.title("Local Chatbot")
    prompt = st.chat_input("Type your message here...")

    if prompt:
        st.session_state.messages_local.append({
            "role": "user",
            "content": prompt
        })
        response = local_llm.local_call(prompt)
        st.session_state.messages_local.append({
            "role": "assistant",
            "content": response
        })

    for msg in st.session_state.messages_local:
        st.chat_message(msg["role"]).write(msg["content"])