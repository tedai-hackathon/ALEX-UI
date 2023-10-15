import streamlit as st
import time

from alex import Alex
from alex.components import setup

if "alex" not in st.session_state:
    st.session_state.alex = Alex()

alex = st.session_state.alex

st.title("Alex")
PAGES = ["Setup", "Chat"]

st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", PAGES)

if "current_page" not in st.session_state:
    st.session_state.current_page = "Setup"

st.session_state.current_page = selected_page

if st.session_state.current_page == "Setup":
    setup(alex.setup_questions, alex)

if st.session_state.current_page == "Chat":
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything about your legal entity"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("Alex"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = alex.chat(prompt)
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
