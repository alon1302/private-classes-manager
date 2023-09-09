from fastapi import FastAPI
from model.models import Lesson, Student

app = FastAPI()

lessons = []

@app.get("/lessons/getAll")
async def root():
    return {"lessons": lessons}

@app.get("/lessons/{student_name}")
async def root(student_name):
    return {"lessons":  [c for c in lessons if c.student_name == student_name] }


@app.post("/lessons/add")
async def add_class(class_item: Lesson):
    lessons.append(class_item)
    return {"message": "class added"}