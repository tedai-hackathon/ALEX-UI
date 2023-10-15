def chat():
    def bot_response(user_message):
        if "[Download PDF]" in user_message:
            pdf_url = user_message.split("](", 1)[1].split(")", 1)[0]
            return f"Bot: You shared a PDF. [Download PDF]({pdf_url})"
        else:
            return f"Bot: You said '{user_message}'"

    # Sidebar
    with st.sidebar:
        st.empty()
        st.empty()

        chat_history = [
            "Chat One",
            "Chat Two",
            "Chat Three",
            "Chat Four",
        ]

        for item in chat_history:
            st.write(item)

        st.markdown("***")

        agree = st.checkbox("File with the Secretary of State")
        agree = st.checkbox("Create your Operating Agreement")
        agree = st.checkbox("Identify your KPIs")
        agree = st.checkbox("More stuff")
        agree = st.checkbox("Even more stuff")

        if agree:
            st.write("Great!")

    # Chat
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    chat_container = st.container()
    user_input = st.text_input("You:", "")
    if st.button("Send"):
        user_message = user_input.strip()
        st.session_state.chat_history.append(f"You: {user_message}")
        bot_reply = bot_response(user_message)
        st.session_state.chat_history.append(bot_reply)

    uploaded_file = st.file_uploader("Upload a File", type=["pdf"])
    if uploaded_file:
        st.session_state.chat_history.append("User uploaded a file.")

    for message in st.session_state.chat_history:
        chat_container.write(message)
