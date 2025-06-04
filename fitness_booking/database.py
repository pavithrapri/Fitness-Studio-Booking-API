import sqlite3

DB_NAME = "fitness.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date_time TEXT NOT NULL,
        instructor TEXT NOT NULL,
        available_slots INTEGER NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        class_id INTEGER,
        client_name TEXT,
        client_email TEXT,
        FOREIGN KEY(class_id) REFERENCES classes(id)
    )''')

    conn.commit()
    conn.close()
