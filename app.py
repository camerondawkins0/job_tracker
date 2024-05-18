import streamlit as st
import random
from database import init_db
import navigation_funcs as nav

random.seed()
# This is the main page and will display summary statistics of the user's job applications
# i.e number of applications, number of interviews, number of offers, etc.
# last job applied for or jobs that are currently in the pipeline (tagged as "In Progress" <- Default status)

# This page will also have a button to add a new job application that will jump to the
# appropriate page for adding a new job application and etc.


st.set_page_config(page_title="Home", page_icon=":moneybag:", layout="wide")
st.write("Welcome to Your Personal Job Tracker!")

init_db()

nav.nav_bar(left=("Apply", "pages/1_Apply.py"),
           middle=("Update", "pages/2_Update.py"),
           right=("Data", "pages/3_Data.py"))

