from utils import db
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
        return "Hello, world!"

@app.get("/root/{name}")
def hello(name):
        return f"Hello {name}"

@app.get("/list")
async def show_list():
        return db

@app.get("/student_db/{student_id}")
async def get_student(student_id):
        for student in db:
                if student["student_id"] == student_id:
                        return student

@app.post("/student_db")
async def add_student(student_id, student_name):
        student = {
                "student_id": student_id,
                "student_name": student_name
        }
        db.append(student)
        return "Successfully added"

@app.put("/student_db/{student_id}")
async def update_student(student_id, student_name):
        for student in db:
                if student["student_id"] == student_id:
                        student["student_name"] = student_name
        return "Successfully updated"

@app.delete("/student_db/{student_id}")
async def remove_student(student_id):
        for student in db:
                if student["student_id"] == student_id:
                        db.remove(student)
        return "Successfully removed"
