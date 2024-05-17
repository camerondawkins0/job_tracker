import sqlite3
from constants.tags import TAGS

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
                application_date TEXT,
                application_status TEXT CHECK(application_status IN ({", ".join(f"'{tag}'" for tag in TAGS)})) DEFAULT "Applied",
                notes TEXT
            );
        ''')
    conn.close()

def insert_application(company_name, job_title, location, salary, hourly, pay_frequency, application_date, application_status, notes):
    conn = get_db_connection()
    with conn:
        conn.execute('''
            INSERT INTO applications (company_name, job_title, location, salary, hourly, pay_frequency, application_date, application_status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (company_name, job_title, location, salary, hourly, pay_frequency, application_date, application_status, notes))
    conn.close()
    
    
