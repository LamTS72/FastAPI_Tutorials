import string
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class Student(BaseModel):
        id: str
        name: str
        gender: str
        age: int

db = [
        Student(
                id="12345",
                name="A",
                gender="Male",
                age=20
        )
]

app = FastAPI()

@app.get("/student_db/{student_id}")
async def get_student(student_id):
        for student in db:
                if student.id == student_id:
                        return student
        raise HTTPException(status_code=404, detail="Not Found")

@app.post("/student_db")
async def add_student(student: Student):
        db.append(student)
        return student
