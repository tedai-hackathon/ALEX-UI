import streamlit as st
import pandas as pd

page_names = ["Home", "Chat", "Dashboard", "Form", "Setup Wizard"]
selected_page = "Home"

if selected_page == "Home":
    st.write(
        '<div style="display: flex; justify-content: center;">', unsafe_allow_html=True
    )
    selected_page = st.selectbox("Select a page:", page_names, key="select_page")

if selected_page == "Chat":

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
elif selected_page == "Dashboard":
    user_business_type = "LLC"
    data = {
        "Company Name": [
            "Company A",
            "Company B",
            "Company C",
            "Company D",
            "Company E",
        ],
        "Business Type": ["Retail", "Technology", "Retail", "Technology", "Healthcare"],
        "Website": [
            "https://companyA.com",
            "https://companyB.com",
            "https://companyC.com",
            "https://companyD.com",
            "https://companyE.com",
        ],
        "Similarity Score": [70, 80, 65, 85, 60],
    }
    df = pd.DataFrame(data)
    pdf_data = {
        "Document 1": "path_to_pdf1.pdf",
        "Document 2": "path_to_pdf2.pdf",
        "Document 3": "path_to_pdf3.pdf",
    }

    # Business Information Table
    st.header("Business Information Table")
    user_similarity_score = st.slider("Similarity Score Filter", 0, 100, 50, 5)
    filtered_data = df[df["Similarity Score"] >= user_similarity_score]
    filtered_data = filtered_data.sort_values(by=["Similarity Score"], ascending=False)
    if not filtered_data.empty:
        st.table(filtered_data)
    else:
        st.info("No similar companies found based on your criteria.")

    # KPIS
    kpi_data = {
        "KPI Name": ["Revenue", "Profit Margin", "Customer Satisfaction", "Churn Rate"],
        "Current Value": [1000000, 0.25, 90, 5],
        "Target Value": [1200000, 0.30, 95, 4],
    }
    df = pd.DataFrame(kpi_data)
    df["Percentage"] = (df["Current Value"] / df["Target Value"] * 100).apply(
        lambda x: f"{x:.2f}"
    )
    st.header("Key Performance Indicators (KPIs) for Your Business")
    st.table(df)

    # DOCUMENTATION
    def download_pdf(pdf_data, filename):
        st.header("Download")
        st.markdown(
            f"Download your {filename} as a PDF file: [Download {filename}]"
            + f"(data:application/pdf;base64,{pdf_data.decode('utf-8')})",
            unsafe_allow_html=True,
        )

    st.header("Documentation")
    col1, col2, col3 = st.columns(3)
    st.markdown("<style>.css-16a0wkx { padding: 0; }</style>", unsafe_allow_html=True)
    if col1.button("  Filing Form  "):
        with open("path_to_filing_form.pdf", "rb") as file:
            pdf_data = file.read()
        col1.markdown(download_pdf(pdf_data, "Filing Form"), unsafe_allow_html=True)

    if col2.button("  Bylaws  "):
        with open("path_to_operating_agreement.pdf", "rb") as file:
            pdf_data = file.read()
        col2.markdown(
            download_pdf(pdf_data, "Operating Agreement / Bylaws"),
            unsafe_allow_html=True,
        )

    if col3.button("  Certificate of Good Standing  "):
        with open("path_to_certificate_of_good_standing.pdf", "rb") as file:
            pdf_data = file.read()
        col3.markdown(
            download_pdf(pdf_data, "Certificate of Good Standing"),
            unsafe_allow_html=True,
        )
elif selected_page == "Form":
    st.title("Questionaire")
    st.text("Please fill out the following form")

    pages_name = "Form", "LLC", "S-corp", "C-Corp", "501c3"
    selected_page = "Form"

    if selected_page == "Form":
        with st.form("alex"):
            name = st.text_input("What is the name of your business?")
            address = st.text_input("What's your physical business address?")
            has_ip = st.text_input("Does your business own any intellectual property?")
            business_type = st.selectbox(
                "What type of business would you like to form?",
                (
                    "Select one",
                    "LLC",
                    "S-CORP",
                    "C-CORP",
                    "501c3",
                    "Sole Proprietorship",
                ),
            )

            if business_type == "C-CORP":
                name = st.text_input("What is the name of your C-CORP?")

            if business_type == "LLC":
                business_type = st.selectbox(
                    "Is your LLC a multi-member or single member?",
                    ("Single-Member", "Multi-Member"),
                )

            submit = st.form_submit_button("Submit")
elif selected_page == "Setup Wizard":
    st.title("Setup Wizard")
    st.text("Please fill out the following form")

    all_business_types = ["LLC", "S-CORP", "C-CORP", "501c3", "Sole Propetiership"]
    optimal_business_type = "To be determined"
    selected_type = st.selectbox(
        "Select Business Type",
        [optimal_business_type]
        + [type for type in all_business_types if type != optimal_business_type],
    )
    st.write(f"Selected Business Type: {selected_type}")

    with st.form("wizard"):
        selected_terms = []
        isNonProfit = "No"
        isNonprofit = st.selectbox(
            "Is your organization a nonprofit",
            (
                "Yes",
                "No",
            ),
        )

        if isNonprofit == "Yes":
            nonProfitType = st.selectbox(
                "What type of nonprofit are you making?",
                (
                    "Religious",
                    "public-benefit",
                ),
            )
            selected_terms.append("non-profit")
            selected_terms.append(nonProfitType)

        if isNonprofit == "No":
            local_selected_terms = []

            term_options = [
                "operating-agreement",
                "manager-managed",
                "member-managed",
                "board",
                "partnership-agreement",
                "partnership",
                "limited-partner",
                "stock",
                "informal",
                "small business partnership",
                "family",
                "restrict-resignation",
                "restrict-transferable-interests-assets",
                "transferable-interests-assets",
                "mutual-benefit",
                "public-benefit",
                "restrict-dissolution",
                "liable-partner",
                "automated-management",
                "smart-contract",
                "restrict-return-capital-contributions",
                "blockchain",
            ]

            st.write("Select the terms you want to classify:")
            for term in term_options:
                selected = st.checkbox(term)
                if selected:
                    local_selected_terms.append(term)

            st.write("Selected Terms:", local_selected_terms)

        submit = st.form_submit_button("Submit")
