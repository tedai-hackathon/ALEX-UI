import streamlit as st
import time
import os

from alex import Alex
from alex.components import setup

if "alex" not in st.session_state:
    st.session_state.alex = Alex()

if "finished_setup" not in st.session_state:
    st.session_state.finished_setup = False

if "filled_form" not in st.session_state:
    st.session_state.filled_form = False

alex = st.session_state.alex

st.title("Alex")
PAGES = ["Setup", "Chat"]

st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", PAGES)

if "current_page" not in st.session_state:
    st.session_state.current_page = "Setup"

st.session_state.current_page = selected_page

if st.session_state.current_page == "Setup":
    if not st.session_state.finished_setup:
        st.session_state.answers = setup(alex.setup_questions, alex)
    else:
        if not st.session_state.filled_form:
            st.write("Please enter your information.")
            form = alex.form
            fields = form.fields
            for field in fields:
                if "Registered Agent" not in field and "RA" not in field:
                    fields[field] = st.text_input(label=field)
            if st.button("Submit"):
                form.fields = fields
                form.save()
                st.session_state.filled_form = True
        else:
            st.write("Please review and sign your filled form.")
            st.download_button(
                label="Download Form",
                data=alex.form.path,
                file_name=os.path.basename(alex.form.path),
                mime="application/pdf",
            )
            st.file_uploader(label="Upload Signed Form")


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
