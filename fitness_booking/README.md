#  Fitness Studio Booking API

A Python FastAPI application to manage fitness class schedules and bookings. The API allows users to view available classes, book a class, and view bookings by email — with support for timezone adjustments.

---

## Features

- List all upcoming classes with optional timezone conversion
- Book a spot in a class if slots are available
- View all bookings for a given email address
- Swagger UI for interactive API testing
- Error handling for overbooking, validation, and missing fields

---

## Tech Stack

- **Language**: Python 3.9+
- **Framework**: FastAPI
- **Database**: SQLite (in-memory)
- **Docs UI**: Swagger (via FastAPI)
- **Timezone Management**: pytz

---

##  Setup Instructions

### 1. Install Dependencies

pip install -r requirements.txt

##  Run the Application

uvicorn main:app --reload

## Access Swagger UI
Visit: http://127.0.0.1:8000/docs

You’ll see all endpoints, parameters, and schemas listed in Swagger for interactive testing.
