import streamlit as st
import os
from gemini_api import CustomGeminiAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Custom Gemini Chatbot", page_icon="🤖")

st.title("🤖 Sanket’s Text-based GeminiAssist")
st.caption("Built with Streamlit + LangChain + Gemini")

# Initialize Gemini API
try:
    gemini = CustomGeminiAPI(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    st.error(str(e))
    st.stop()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini response
    response = gemini.generate(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
