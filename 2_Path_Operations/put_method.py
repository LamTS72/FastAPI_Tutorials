from utils import db
from fastapi import FastAPI


app = FastAPI()

@app.put("/student_db/{student_id}")
async def update_student(student_id, student_name):
        for student in db:
                if student["student_id"] == student_id:
                        student["student_name"] = student_name
        