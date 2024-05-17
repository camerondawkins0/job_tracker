import streamlit as st
import sqlite3
import pandas as pd
from app import navigation
from database import get_db_connection

# Here you can update the fields of your applications as they progress through the hiring process.
# Or remove applications that are no longer relevant.

conn = sqlite3.connect('job_tracker.db')
c = conn.cursor()

# Page layout
st.title("Update Job Applications")
st.markdown("""Use this page to update your job applications. You edit the fields directly in the table below.
            Then click 'Submit' to save your changes.""")


# Load data
c.execute("SELECT * FROM applications")
data = c.fetchall()
df = pd.DataFrame(data, columns=["application_id", "company", "job_title", "location", "salary",
                                 "hourly", "pay_frequency", "application_date", "application_status", "notes"])

# Display data
edited_df = st.data_editor(df, key="applications", num_rows="dynamic",
                           hide_index=True, use_container_width=True)

def update_database(changes):
    conn = get_db_connection()
    # cursor = conn.cursor()
    for row_index, updated_values in changes.items():
        set_clause = ", ".join([f"{col} = ?" for col in updated_values.keys()])
        values = list(updated_values.values())
        values.append(int(row_index))  # Assuming 'id' is the primary key
        query = f"UPDATE applications SET {set_clause} WHERE application_id = ?"
        conn.execute(query, values)
    conn.commit()
    conn.close()

if st.button("Submit"):
    changes = st.session_state["applications"]["edited_rows"]
    if len(changes) <= 1:
        st.write(f"updating a single row")
    else:
        st.write("Updating multiple rows!")
    update_database(changes)
    st.session_state["applications"]["edited_rows"].clear()
        
st.write(st.session_state["applications"])

# # Visualization
# status_counts = df["status"].value_counts()
# st.bar_chart(status_counts)

navigation(left=("Home", "app.py"),
           middle=("Apply", "pages/1_Apply.py"),
           right=("Data", "pages/3_Data.py"))