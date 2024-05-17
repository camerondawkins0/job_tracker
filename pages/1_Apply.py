import streamlit as st
from app import navigation
# Here is were all the pertinient information will be entered by the user to sumbit their application.

st.set_page_config(page_title="Apply", page_icon=":clipboard:", layout="wide")

with st.form("application_form"):
    st.write("Please enter the following information to submit your job application.")
    job_title = st.text_input("Job Title")
    company_name = st.text_input("Company Name")
    location = st.text_input("Location")
    date_applied = st.date_input("Date Applied")
    status = st.selectbox("Status", ["Applied", "In Progress", "Interview", "Offer", "Rejected"], key="form")
    notes = st.text_area("Notes")
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        st.write("Your application has been submitted!")





navigation(left=("Home", "app.py"),
           middle=("Update", "pages/2_Update.py"),
           right=("Data", "pages/3_Data.py"))