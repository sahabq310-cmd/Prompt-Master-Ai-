import streamlit as st
import google.generativeai as genai

st.title("Billionaire Mentor AI")

# API Key load karo
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Model setup
model = genai.GenerativeModel("gemini-pro")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history dikhao
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Apni business problem yahan likho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ka response
    try:
        response = model.generate_content(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
