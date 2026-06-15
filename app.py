import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(page_title="Billionaire Mentor AI", page_icon="💡")
st.title("💡 Billionaire Mentor AI")

# API Key check
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets mein GOOGLE_API_KEY set nahi hai!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Model definition (sabse basic aur stable)
try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Model load karne mein error: {e}")
    st.stop()

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Apni business problem yahan likho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Response
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Model Error: API Key check karo ya model name change karo.")
            st.write(f"Details: {e}")            st.error("Model error: Check your API Key or try a different model name.")
            st.write(str(e))
