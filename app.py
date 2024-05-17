import streamlit as st
import random

random.seed(42)
# This is the main page and will display summary statistics of the user's job applications
# i.e number of applications, number of interviews, number of offers, etc.
# last job applied for or jobs that are currently in the pipeline (tagged as "In Progress" <- Default status)

# This page will also have a button to add a new job application that will jump to the
# appropriate page for adding a new job application and etc.


st.set_page_config(page_title="Home", page_icon=":moneybag:", layout="wide")
st.write("Welcome to Your Personal Job Tracker!")

def generate_keys(num_keys: int = 3):
    keys = [str(random.randint(1, 1000)) for i in range(num_keys)]
    return keys

def navigation(keys: set = generate_keys(), left: tuple[str, str] = None,
               middle: tuple[str, str] = None,
               right: tuple[str, str] = None):

    """Creates a navigation bar with three buttons.
    
    Params:
        key (str): A unique key for the navigation bar.
        
        left (tuple): A tuple containing the button label and the page path.
        
        middle (tuple): A tuple containing the button label and the page path.
        
        right (tuple): A tuple containing the button label and the page path.
        
    Raises:
        ValueError: If no key is provided.
    
    Returns:
        None
    """
    

    col_1, col_2, col_3 = st.columns([1, 1, 1])
    
    with col_1:
        if st.button(left[0], key=keys[0]):
            st.switch_page(left[1])
    with col_2:
        if st.button(middle[0], key=keys[1]):
            st.switch_page(middle[1])
    with col_3:
        if st.button(right[0], key=keys[2]):
            st.switch_page(right[1])
    
    keys.clear()
            
navigation(left=("Apply", "pages/1_Apply.py"), middle=("Update", "pages/2_Update.py"), right=("Data", "pages/3_Data.py"))

