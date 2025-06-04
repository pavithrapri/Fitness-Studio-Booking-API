from fastapi import FastAPI, HTTPException, Query
from database import init_db, get_connection
from models import ClassOut, BookingIn, BookingOut
from utils import convert_to_timezone
from seed_data import seed_classes
from typing import List

app = FastAPI(title="Fitness Studio Booking API")

init_db()
seed_classes()

@app.get("/classes", response_model=List[ClassOut])
def list_classes(timezone: str = Query("Asia/Kolkata")):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes")
    classes = cursor.fetchall()
    conn.close()

    result = []
    for c in classes:
        result.append({
            "id": c[0],
            "name": c[1],
            "date_time": convert_to_timezone(c[2], timezone),
            "instructor": c[3],
            "available_slots": c[4]
        })
    return result

@app.post("/book", response_model=BookingOut)
def book_class(booking: BookingIn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT available_slots FROM classes WHERE id = ?", (booking.class_id,))
    row = cursor.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Class not found")

    if row[0] <= 0:
        raise HTTPException(status_code=400, detail="No available slots")

    cursor.execute("""
        INSERT INTO bookings (class_id, client_name, client_email)
        VALUES (?, ?, ?)
    """, (booking.class_id, booking.client_name, booking.client_email))

    cursor.execute("""
        UPDATE classes SET available_slots = available_slots - 1 WHERE id = ?
    """, (booking.class_id,))
    conn.commit()

    booking_id = cursor.lastrowid
    conn.close()

    return {
        "id": booking_id,
        **booking.dict()
    }

@app.get("/bookings", response_model=List[BookingOut])
def get_bookings(email: str = Query(...)):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM bookings WHERE client_email = ?
    """, (email,))
    bookings = cursor.fetchall()
    conn.close()

    return [{
        "id": b[0],
        "class_id": b[1],
        "client_name": b[2],
        "client_email": b[3]
    } for b in bookings]
