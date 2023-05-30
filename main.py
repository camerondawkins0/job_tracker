import streamlit as st
import pandas as pd
import datetime as datetime
from helperFunctions.dBCommands import connect_to_db, close_db



cursor, conn = connect_to_db()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")    
st.markdown("# Where'd You Apply?")

create_table_query = '''
CREATE TABLE IF NOT EXISTS job_details (
    id INTEGER PRIMARY KEY,
    company_name TEXT,
    job_title TEXT,
    city TEXT,
    state TEXT,
    salary INTEGER,
    date TEXT
)
'''
cursor.execute(create_table_query)

# Define the Streamlit form
with st.form(key="apply_form"):
    st.markdown("## Enter Job Details")
    
    company_name = st.text_input("Company Name")
    job_title = st.text_input("Job Title")
    city = st.text_input("City", value='Remote')
    state = st.text_input("State", value='Remote')
    salary = st.text_input("Salary", value='N/A')
    date = st.date_input("Date", value=datetime.date.today())


    if st.form_submit_button("Submit"):
        st.success("You're one step closer!")
        
        # Insert the job details into the table
        insert_query = '''
        INSERT INTO job_details (company_name, job_title, city, state, salary, date)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(insert_query, (company_name, job_title, city, state, salary, date))
        conn.commit()

col1, col2, col3 = st.columns(3, gap="large")
with col1:
    if st.button("Close Database"):
    # Close the cursor and connection
        close_db()
with col2:
    if st.button("Open Database"):
        cursor, conn = connect_to_db()
with col3:
    if st.button("Close Application"):
        st.stop()
