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
                myBusiness.add_manager(st.text_input("Person 1"), 0)
                myBusiness.add_manager(st.text_input("Person 2"), 0)
                myBusiness.add_manager(st.text_input("Person 3"), 0)
                myBusiness.add_manager(st.text_input("Person 4"), 0)
        if business_type == "S-CORP":
            scorp_type = st.selectbox(
                "Is your S-CORP a multi-member or single member",
                ("Select one", "Single-Member", "Multi-Member"),
            )
            if scorp_type == "Multi-Member":
                st.header("Type Stakeholders' names & percentage of the company")
                myBusiness.add_manager(st.text_input("Person 1"), 0)
                myBusiness.add_manager(st.text_input("Person 2"), 0)
                myBusiness.add_manager(st.text_input("Person 3"), 0)
                myBusiness.add_manager(st.text_input("Person 4"), 0)
        if business_type == "501c3":
            st.header(
                "Please declare all members on your board of directors (3 minimum)"
            )
            myBusiness.add_manager(st.text_input("Person 1"), 0)
            myBusiness.add_manager(st.text_input("Person 2"), 0)
            myBusiness.add_manager(st.text_input("Person 3"), 0)
            myBusiness.add_manager(st.text_input("Person 4"), 0)
        if business_type == "LLC":
            llc_type = st.selectbox(
                "Is your LLC a multi-member or single member",
                ("Select one", "Single-Member", "Multi-Member"),
            )
            if llc_type == "Multi-Member":
                st.text("Type Stakeholders' names & percentage of the company")
                myBusiness.add_manager(st.text_input("Person 1"), 0)
                myBusiness.add_manager(st.text_input("Person 2"), 0)
                myBusiness.add_manager(st.text_input("Person 3"), 0)
                myBusiness.add_manager(st.text_input("Person 4"), 0)

        st.form_submit_button("Submit")

        if business_type == "Unsure":
            setUpWizard(False)
