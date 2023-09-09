from pydantic import BaseModel
from typing import Dict

class Student(BaseModel):
    name: str
    grade: str
    subject_to_price: Dict[str, int]