def dashboard():
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
    kpi_data = myBusiness.kpiData
    df = pd.DataFrame(kpi_data)

    if not df.empty:
        # Calculate the "Percentage" column if the DataFrame is not empty
        df["Percentage"] = (df["current_value"] / df["target_value"] * 100).apply(
            lambda x: f"{x:.2f}"
        )
        st.header("Key Performance Indicators (KPIs) for Your Business")
        st.table(df)
    else:
        st.info("No KPI data available.")

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
    if col1.button("  Filing Form  "):
        with open("path_to_filing_form.pdf", "rb") as file:
            pdf_data = file.read()
        download_pdf(pdf_data, "Filing Form")

    if col2.button("  Bylaws  "):
        with open("path_to_operating_agreement.pdf", "rb") as file:
            pdf_data = file.read()
        download_pdf(pdf_data, "Operating Agreement / Bylaws")

    if col3.button("  Certificate of Good Standing  "):
        with open("path_to_certificate_of_good_standing.pdf", "rb") as file:
            pdf_data = file.read()
        download_pdf(pdf_data, "Certificate of Good Standing")
