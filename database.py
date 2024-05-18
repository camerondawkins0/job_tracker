import sqlite3
import pandas as pd
from constants.tags import APP_TAGS, COL_TAGS

# important database functions will exist here for handling the data and accessing the database

def get_db_connection():
    conn = sqlite3.connect('job_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.executescript(f'''
            CREATE TABLE IF NOT EXISTS applications (
                application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                job_title TEXT NOT NULL,
                location TEXT,
                salary INTEGER,
                hourly BOOLEAN,
                pay_frequency TEXT,
                application_date DATE NOT NULL,
                application_status TEXT CHECK(application_status IN ({", ".join(f"'{tag}'" for tag in APP_TAGS)})) DEFAULT "Applied",
                notes TEXT
            );
        ''')
    conn.close()

def fetch_data(columns: list = None):
    conn = get_db_connection()
    with conn:
        if columns is None:
            query = "SELECT * FROM applications"
        else:
            query = f"SELECT {', '.join(columns)} FROM applications"
        cursor = conn.execute(query)
        data = cursor.fetchall()
    conn.close()
    return (data, COL_TAGS) if not columns else (data, columns)

def insert_application(company_name, job_title, location, salary, hourly, pay_frequency, application_date, application_status, notes):
    conn = get_db_connection()
    with conn:
        conn.execute('''
            INSERT INTO applications (company_name, job_title, location, salary, hourly, pay_frequency, application_date, application_status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (company_name, job_title, location, salary, hourly, pay_frequency, application_date, application_status, notes))
    conn.close()
