import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Billionaire Mentor AI")
st.title("Billionaire Mentor AI")

# API Key setup
# Note: GitHub par "Secrets" mein GOOGLE_API_KEY set karna mat bhoolna
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# System Instruction
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Tum ek expert Business Mentor ho. Mera maqsad multi-billionaire banna hai. Mujhe hamesha high-value, actionable, aur practical advice do. Jawab concise rakho aur bullet points ya tables ka use karo."
)

# Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Apni business problem yahan likho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
