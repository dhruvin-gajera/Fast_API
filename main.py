from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name:str
    age:int
    yera:str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(name:str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name is not None:
        students[student_id]["name"] = student.name

    if student.age is not None:
        students[student_id]["age"] = student.age

    if student.year is not None:
        students[student_id]["year"] = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": "Student deleted successfully"}