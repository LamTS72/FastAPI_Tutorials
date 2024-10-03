from utils import db
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
        return {
                "message": "Hello, world"
        }
@app.get("/list")
async def show_list():
        return db

@app.get("/student_db/{student_id}")
async def get_student(student_id):
        for student in db:
                if student["student_id"] == student_id:
                        return student
                
