from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ClassOut(BaseModel):
    id: int
    name: str
    date_time: str
    instructor: str
    available_slots: int

class BookingIn(BaseModel):
    class_id: int
    client_name: str = Field(..., min_length=1)
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: str
