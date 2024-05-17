import sqlite3

# important database functions will exist here for handling the data and accessing the database

def get_db_connection():
    conn = sqlite3.connect('job_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS applications (
                application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                job_title TEXT NOT NULL,
                location TEXT,
                salary INTEGER,
                application_date TEXT,
                application_status TEXT CHECK(application_status IN ('applying', 'applied', 'interview', 'rejection', 'offer', 'accepted')),
                contact_email TEXT
            );
        ''')
    conn.close()
