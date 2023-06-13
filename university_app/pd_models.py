from pydantic import BaseModel
import datetime

class StudentIn(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    group_id: int

class StudentOut(StudentIn):
    id: int

    class Config:
        orm_mode = True

class TeacherOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    department_id: int

    class Config:
        orm_mode = True

class СourseIn(BaseModel):
    title: str
    teacher_id: int
    group_id: int
    semester_id: int

class СourseOut(СourseIn):
    id: int

    class Config:
        orm_mode = True

class GradeIn(BaseModel):
    value: int
    date: datetime.date
    exam_id: int
    student_id: int

class GradeCreateByCourse(BaseModel):
    value: int
    date: datetime.date
    course_id: int
    student_id: int


class GradeOut(GradeIn):
    id: int

    class Config:
        orm_mode = True 



