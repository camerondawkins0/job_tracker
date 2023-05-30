import sqlite3

def connect_to_db():
    conn = sqlite3.connect('./data/jobs_data.db')
    cursor = conn.cursor()
    return cursor, conn


def close_db():
    cursor.close()
    conn.close()