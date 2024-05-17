import streamlit as st
from app import navigation

# Here is where data can be accessed for more in-depth analysis and exploration
# Will also be able to export this data to a CSV file or Excel file
# Visualizations can be created here as well

navigation(left=("Home", "../app.py"),
           middle=("Apply", "pages/1_Apply.py"),
           right=("Update", "pages/2_Update.py"))