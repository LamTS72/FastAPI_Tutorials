from utils import db
from fastapi import FastAPI


app = FastAPI()

@app.post("/student_db")
async def add_student(student_id, student_name):
        student = {
                "student_id": student_id,
                "student_name": student_name
        }
        db.append(student)
        return "Successfully added"