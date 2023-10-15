def setUpWizard(isForm):
    st.title("Setup Wizard")
    st.text(
        "The setup wizard will help you decide the optimal business"
        + "structure for your business."
        + "You may override its suggestion."
    )

    all_business_types = ["LLC", "S-CORP", "C-CORP", "501c3", "Sole Proprietorship"]
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
                        selected_terms.append(term)

                st.write("Selected Terms:", selected_terms)
            submit = st.form_submit_button("Submit")
            if submit:
                st.text("Form submitted")

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
                    selected_terms.append(term)

            st.write("Selected Terms:", selected_terms)
