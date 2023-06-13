from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from typing import List
from models import SessionLocal, Student, Grade, HomeworkGrade, AssignmentGrade, Teacher, Course, Group, Grade, Exam
from pd_models import StudentIn, StudentOut, TeacherOut, СourseIn, СourseOut, GradeIn, GradeOut, GradeCreateByCourse
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST /students - создать нового студента.
@app.post("/students", response_model=StudentOut)
def create_student(student: StudentIn, db: Session = Depends(get_db)):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# GET /students/{student_id} - получить информацию о студенте по его id.
@app.get("/students/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студента с указанным id нет")
    return student

#PUT /students/{student_id} - обновить информацию о студенте по его id.
@app.put("/students/{student_id}", response_model=StudentOut)
def update_student(student_id: int, updated_student: StudentIn ,db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студента с указанным id нет")
    for field, value in updated_student:
        print(f'{field}: {value}')
        setattr(student, field, value)
    db.commit()
    db.refresh(student)
    return student

#DELETE /students/{student_id} - удалить студента по его id.
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студента с указанным id нет")
    db.query(Grade).filter(Grade.student_id == student_id).delete()
    db.query(HomeworkGrade).filter(HomeworkGrade.student_id == student_id).delete()
    db.query(AssignmentGrade).filter(AssignmentGrade.student_id == student_id).delete()
    db.delete(student)
    db.commit()
    return {"message": "Студент удален"}

#GET /teachers - получить список всех преподавателей.
@app.get("/teachers", response_model=List[TeacherOut])
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).all()
    return teachers

#POST /courses - создать новый курс.
@app.post("/courses", response_model=СourseOut)
def create_course(course: СourseIn, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# GET /courses/{course_id} - получить информацию о курсе по его id.
@app.get("/courses/{course_id}", response_model=СourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Курса с указанным id нет")
    return course

# GET /courses/{course_id}/students - получить список всех студентов на курсе.
@app.get("/courses/{course_id}/students", response_model=List[StudentOut])
def get_students_on_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Курса с указанным id нет")
    
    students = db.query(Student).join(Group).filter(Group.id == course.group_id).all()
    return students

# POST /grades - создать новую оценку для студента по курсу.
@app.post("/grades", response_model=GradeOut)
def create_grade(grade: GradeCreateByCourse, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == grade.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    course = db.query(Course).filter(Course.id == grade.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Курс не найден")
    if course.group_id != student.group_id:
        raise HTTPException(status_code=400, detail="Студент не принадлежит данному курсу")
    if course.exams:
        exam_id= course.exams[0].id
    else:
        raise HTTPException(status_code=404, detail="Экзамен для данного курса не создан")
    new_grade = Grade(value=grade.value, date=grade.date, exam_id=exam_id, student_id=grade.student_id)
    db.add(new_grade)
    db.commit()
    db.refresh(new_grade)
    return new_grade


# PUT /grades/{grade_id} - обновить оценку студента по курсу.
@app.put("/grades/{grade_id}", response_model=GradeOut)
def update_garde(grade_id: int, updated_grade: GradeIn, db: Session = Depends(get_db)):
    garde = db.query(Grade).filter(Grade.id == grade_id).first()
    if not garde:
        raise HTTPException(status_code=404, detail="Оценки с указанным id нет")
    exam = db.query(Exam).filter(Exam.id == updated_grade.exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамена с указанным id нет")
    student = db.query(Student).filter(Student.id == updated_grade.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студента с указанным id нет")
    course = db.query(Course).filter(Course.id == exam.course_id).first()
    if course.group_id != student.group_id:
        raise HTTPException(status_code=400, detail="Студент не принадлежит данному курсу (экзамену)")
    for field, value in updated_grade:
        setattr(garde, field, value)
    db.commit()
    db.refresh(garde)
    return garde