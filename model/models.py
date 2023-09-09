from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class Student(BaseModel):
    name: str
    grade: str
    subject_to_price: Dict[str, int]

class Lesson(BaseModel):
    student_name: str
    subject: str
    location: str
    start_time: datetime
    duration: float
    total_price: int
    payment_method: str
    is_paid: bool
    notes: str

