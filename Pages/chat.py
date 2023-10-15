def chatPage():
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

    chat_bot = Chat(docs_dir="docs", db_dir="db", urls=["https://apple.com"])
    
    # Create a Streamlit container for the chat interface
    chat_container = st.container()
    
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        user_message = user_input.strip()
        st.session_state.chat_history.append(f"You: {user_message}")
        
        try:
            # Call the chat method of the Chat object to get a response
            bot_reply = chat_bot.chat(user_message)
            st.session_state.chat_history.append(f"Bot: {bot_reply}")
        except Exception as e:
            # Log and display any errors that occur during the AI interaction
            st.session_state.chat_history.append(f"Bot Error: {str(e)}")

    uploaded_file = st.file_uploader("Upload a File", type=["pdf"])
    
    if uploaded_file:
        st.session_state.chat_history.append("User uploaded a file.")

    for message in st.session_state.chat_history:
        chat_container.write(message)
