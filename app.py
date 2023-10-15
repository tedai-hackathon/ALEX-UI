import streamlit as st
import pandas as pd
import chat
import dashboard
import form
import setUpWizard

# PAGE CONDITIONAL FOR CHANGING PAGES BASED ON SELECTION
def pageConditional():
    global selected_page
    page_names = ["Home", "Chat", "Dashboard", "Form", "Setup Wizard"]

    if selected_page == "Home":
        selected_page = st.selectbox("Select a page:", page_names, key="select_page")

    if selected_page == "Home":
        st.write(
            '<div style="display: flex; justify-content: center;">',
            unsafe_allow_html=True,
        )

    if selected_page == "Chat":
        Chat()
    elif selected_page == "Dashboard":
        Dashboard()
    elif selected_page == "Form":
        Form()
    elif selected_page == "Setup Wizard":
        setUpWizard(True)


# BUSINESS KPI INITIALIZATION PLACEHOLDER
myBusiness = Business()
myBusiness.add_kpi("User Engagement", 1000, 1500)
myBusiness.add_kpi("App Downloads", 5000, 8000)
myBusiness.add_kpi("Daily Active Users (DAU)", 2000, 3000)
myBusiness.add_kpi("User Retention Rate", 85, 90)
myBusiness.add_kpi("User Acquisition Cost", 2.5, 2.0)
myBusiness.add_kpi("Monthly Revenue", 15000, 20000)
myBusiness.add_kpi("Bug Fix Response Time", 3, 2)
myBusiness.add_kpi("Feature Release Frequency", 1, 2)

page_names = ["Home", "Chat", "Dashboard", "Form", "Setup Wizard"]
selected_page = "Home"

pageConditional()
