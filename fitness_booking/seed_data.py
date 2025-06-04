from database import get_connection

def seed_classes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM classes")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO classes (name, date_time, instructor, available_slots)
        VALUES (?, ?, ?, ?)
        """, [
            ("Yoga", "2025-06-05T10:00:00", "Alice", 5),
            ("Zumba", "2025-06-05T17:00:00", "Bob", 8),
            ("HIIT", "2025-06-06T09:00:00", "Charlie", 6)
        ])
        conn.commit()
    conn.close()
