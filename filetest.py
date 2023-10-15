import streamlit as st
import pandas as pd

page_names = ["Home", "Chat", "Dashboard", "Form", "Setup Wizard"]
selected_page = "Home"


class Business:
    def __init__(self):
        self.name = ""
        self.business_type = ""
        self.address = ""
        self.has_ip = ""
        self.explanation = ""
        self.goals = ""
        self.singleOrMulti = ""
        self.managers = []
        self.kpis = []
        self.terms = []
        self.isNonProfit = False

    def add_manager(self, manager_name, percentage):
        self.managers.append({"name": manager_name, "percentage": percentage})

    def add_kpi(self, kpi_name, current_value, target_value):
        self.kpis.append(
            {
                "name": kpi_name,
                "current_value": current_value,
                "target_value": target_value,
            }
        )

    def add_kpi_data(self, kpi_name, percentage):
        self.kpiData.append({"name": kpi_name, "percentage": percentage})

    def add_organization_term(self, term):
        self.organization_terms.append(term)


def setUpWizard(isForm):
    st.title("Setup Wizard")
    st.text(
        "The setup wizard will help you to decide the optimal business"
        + "structure for your business. You may override its sugegstion."
    )

    all_business_types = ["LLC", "S-CORP", "C-CORP", "501c3", "Sole Propetiership"]
    optimal_business_type = "To be determined"
    selected_type = st.selectbox(
        "Select Business Type",
        [optimal_business_type]
        + [type for type in all_business_types if type != optimal_business_type],
    )
    st.write(f"Selected Business Type: {selected_type}")
    if isForm:
        with st.form("wizard"):
            selected_terms = []
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
                myBusiness.isNonProfit = False
            else:
                myBusiness.isNonProfit = True

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
            st.text(submit)

            myBusiness.terms = selected_terms
    else:
        selected_terms = []
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


def Form():
    st.title("Questionnaire")
    st.text("Please fill out the following form")

    with st.form("alex"):
        myBusiness.name = st.text_input("What is the name of your business?")
        myBusiness.address = st.text_input("What's your physical business address?")
        myBusiness.has_ip = st.text_input(
            "Does your business own any intellectual property?"
        )
        myBusiness.explanation = st.text_input(
            "Please explain what your business will do."
        )
        myBusiness.goals = st.text_input("What are the goals of your business?")
        myBusiness.business_type = st.selectbox(
            "What type of business would you like to form",
            (
                "Select one",
                "LLC",
                "S-CORP",
                "C-CORP",
                "501c3",
                "Sole Proprietorship",
                "Unsure",
            ),
        )
        business_type = myBusiness.business_type
        if business_type == "C-CORP":
            ccorp_type = st.selectbox(
                "Is your C-CORP a multi-member or single member",
                ("Select one", "Single-Member", "Multi-Member"),
            )
            if ccorp_type == "Multi-Member":
                st.header("Type Stakeholders' names & percentage of the company")
                myBusiness.addManager(st.text_input("Person 1"))
                myBusiness.addManager(st.text_input("Person 2"))
                myBusiness.addManager(st.text_input("Person 3"))
                myBusiness.addManager(st.text_input("Person 4"))
        if business_type == "S-CORP":
            scorp_type = st.selectbox(
                "Is your S-CORP a multi-member or single member",
                ("Select one", "Single-Member", "Multi-Member"),
            )
            if scorp_type == "Multi-Member":
                st.header("Type Stakeholders' names & percentage of the company")
                myBusiness.addManager(st.text_input("Person 1"))
                myBusiness.addManager(st.text_input("Person 2"))
                myBusiness.addManager(st.text_input("Person 3"))
                myBusiness.addManager(st.text_input("Person 4"))
        if business_type == "501c3":
            st.header(
                "Please declare all members on your board of directors (3 minimum)"
            )
            myBusiness.addManager(st.text_input("Person 1"))
            myBusiness.addManager(st.text_input("Person 2"))
            myBusiness.addManager(st.text_input("Person 3"))
            myBusiness.addManager(st.text_input("Person 4"))
        if business_type == "LLC":
            llc_type = st.selectbox(
                "Is your LLC a multi-member or single member",
                ("Select one", "Single-Member", "Multi-Member"),
            )
            if llc_type == "Multi-Member":
                st.text("Type Stakeholders' names & percentage of the company")
                myBusiness.addManager(st.text_input("Person 1"))
                myBusiness.addManager(st.text_input("Person 2"))
                myBusiness.addManager(st.text_input("Person 3"))
                myBusiness.addManager(st.text_input("Person 4"))

        st.form_submit_button("Submit")

        if business_type == "Unsure":
            setUpWizard(False)


def Chat():
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


def Dashboard():
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


def pageConditional():
    page_names = ["Home", "Chat", "Dashboard", "Form", "Setup Wizard"]
    selected_page = "Home"

    if selected_page == "Home":
        st.write(
            '<div style="display: flex; justify-content: center;">',
            unsafe_allow_html=True,
        )
        selected_page = st.selectbox("Select a page:", page_names, key="select_page")
    if selected_page == "Chat":
        Chat()
    elif selected_page == "Dashboard":
        Dashboard()
    elif selected_page == "Form":
        Form()
    elif selected_page == "Setup Wizard":
        setUpWizard(True)


myBusiness = Business()
pageConditional()
