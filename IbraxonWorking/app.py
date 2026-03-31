import streamlit as st
import requests
import os

st.set_page_config(page_title="Ibraxon AI", page_icon="🤖", layout="wide")

st.title("🤖 Ibraxon AI")
st.caption("Your Intelligent Assistant")

# Get API key from environment
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you?"}]

# Display chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                    json={"model": "openai/gpt-3.5-turbo", "messages": st.session_state.messages}
                )
                if response.status_code == 200:
                    reply = response.json()["choices"][0]["message"]["content"]
                    st.write(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                else:
                    st.error("API Error")
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("**Ibrahim Talib** | Computer Science Student | Dushanbe Innovative Institute")