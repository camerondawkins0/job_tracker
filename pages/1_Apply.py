import streamlit as st
from app import navigation
from database import insert_application
from constants.tags import TAGS
# Here is were all the pertinient information will be entered by the user to sumbit their application.

st.set_page_config(page_title="Apply", page_icon=":clipboard:", layout="wide")

with st.form("application_form", clear_on_submit=True):
    st.write("Please enter the following information to submit your job application.")
    job_title = st.text_input("Job Title")
    company_name = st.text_input("Company Name")
    salary = st.number_input("Salary", value=None, min_value=0)
    hourly = st.checkbox("Hourly")
    pay_frequency = st.selectbox("Pay Frequency", ["Weekly", "Bi-Weekly", "Monthly"])
    location = st.text_input("Location")
    date_applied = st.date_input("Date Applied")
    status = st.selectbox("Status", TAGS, key="form")
    notes = st.text_area("Notes")
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        insert_application(company_name, job_title, location, salary,
                            hourly, pay_frequency, date_applied, status, notes)
        st.write("Your application has been submitted!")

navigation(left=("Home", "app.py"),
           middle=("Update", "pages/2_Update.py"),
           right=("Data", "pages/3_Data.py"))
