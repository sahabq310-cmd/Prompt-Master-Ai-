import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Billionaire Mentor AI")
st.title("Billionaire Mentor AI")

# API Key load
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Model setup - Using the standard name
model = genai.GenerativeModel("gemini-1.5-flash")

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Apni business problem yahan likho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Model error: Check your API Key or try a different model name.")
            st.write(str(e))
