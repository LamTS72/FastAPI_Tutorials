from utils import db
from fastapi import FastAPI

app = FastAPI()

@app.delete('/student_db/{student_id}')
async def remove_student(student_id):
        for student in db:
                if student["student_id"] == student_id:
                        db.remove(student)
                        