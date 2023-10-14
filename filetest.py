import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st


# Define page names
page_names = [ "Home", "Chat", "Dashboard"]
selected_page = "Home"


if selected_page == "Home":

    st.write('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
    selected_page = st.selectbox("Select a page:", page_names, key="select_page")

# Define content for each page
if selected_page == "Chat":
    with st.sidebar:
        # Create buttons in the center
        st.empty()
        st.empty()

        text_items = [
            "Chat One",
            "Chat Two",
            "Chat Three",
            "Chat Four",
        ]

        # Display the list of text items
        for item in text_items:
            st.write(item)
        
        st.markdown("***")

        agree = st.checkbox('File with the Secretary of State')
        agree = st.checkbox('Create your Operating Agreement')
        agree = st.checkbox('Identify your KPIs')
        agree = st.checkbox('More stuff')
        agree = st.checkbox('Even more stuff')

        if agree:
            st.write('Great!')
    with st.chat_message("user"):
        st.write("Hello 👋")

    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
elif selected_page == "Dashboard":
    
    # Create a Streamlit sidebar for user inputs
    # Business type determination (You need to replace this with your own logic)
    # Sample logic: If the user's business type is not provided, set it to "Unknown"
    user_business_type = "LLC"
    # Create a sample DataFrame of similar companies
    data = {
        "Company Name": ["Company A", "Company B", "Company C", "Company D", "Company E"],
        "Business Type": ["Retail", "Technology", "Retail", "Technology", "Healthcare"],
        "Website": ["https://companyA.com", "https://companyB.com", "https://companyC.com", "https://companyD.com", "https://companyE.com"],
        "Similarity Score": [70, 80, 65, 85, 60],
    }
    df = pd.DataFrame(data)

    data = {
        "Business Name": ["Company A", "Company B", "Company C"],
        "Description": [
            "Company A is a retail business specializing in electronics.",
            "Company B is a technology company that develops software solutions.",
            "Company C is a healthcare provider offering medical services."],
        "Link": [
            "https://companyA.com",
            "https://companyB.com",
            "https://companyC.com"],
        "Similarity Score": [75, 85, 60]
    }

    # PDF file data
    pdf_data = {
        "Document 1": "path_to_pdf1.pdf",
        "Document 2": "path_to_pdf2.pdf",
        "Document 3": "path_to_pdf3.pdf",
    }

    # Display PDF documents side by side in a row
    st.header("Filing Documents")

    # Check if PDF files are available and display them side by side
    for doc_name, pdf_path in pdf_data.items():
        st.subheader(doc_name)

        try:
            # Open and render the PDF file
            pdf_document = fitz.open(pdf_path)

            # Display each page of the PDF side by side
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                img = page.get_pixmap()
                st.image(img, use_container_width=True)

        except Exception as e:
            st.error(f"Error loading PDF: {str(e)}")

        # Similarity Score slider

    # Display the filtered table
    st.header("Business Information Table")

    user_similarity_score = st.slider("Similarity Score Filter", 0, 100, 50, 5)

    # Filter the data based on the slider value
    filtered_data = df[df["Similarity Score"] >= user_similarity_score]
    filtered_data = filtered_data.sort_values(by=["Similarity Score"], ascending=False)

    if not filtered_data.empty:
        st.table(filtered_data)
    else:
        st.info("No similar companies found based on your criteria.")

    # Sample KPI data (replace with your own data)
    kpi_data = {
        "KPI Name": ["Revenue", "Profit Margin", "Customer Satisfaction", "Churn Rate"],
        "Current Value": [1000000, 0.25, 90, 5],
        "Target Value": [1200000, 0.30, 95, 4],
    }

    # Create a Pandas DataFrame from the KPI data
    df = pd.DataFrame(kpi_data)

    # Calculate the Percentage column
    df["Percentage"] = (df["Current Value"] / df["Target Value"]) * 100

    # Display the KPI table with the Percentage column
    st.header("Key Performance Indicators (KPIs) for Your Business")
    st.table(df)


