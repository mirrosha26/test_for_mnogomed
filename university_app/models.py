from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DATABASE


SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE.get('USER')}:{DATABASE.get('PASSWORD')}@{DATABASE.get('HOST')}/{DATABASE.get('NAME')}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Semester(Base):
    __tablename__ = "semester"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))


class Faculty(Base):
    __tablename__ = "faculty"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))


class Group(Base):
    __tablename__ = "group_"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    faculty_id = Column(Integer, ForeignKey("faculty.id"))
    faculty = relationship("Faculty", backref="groups")


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)
    group_id = Column(Integer, ForeignKey("group_.id"))
    group = relationship("Group", backref="students")


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    faculty_id = Column(Integer, ForeignKey("faculty.id"))
    faculty = relationship("Faculty", backref="departments")


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("department.id"))
    department = relationship("Department", backref="teachers")


class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    group_id = Column(Integer, ForeignKey("group_.id"))
    semester_id = Column(Integer, ForeignKey("semester.id"))
    teacher = relationship("Teacher", backref="courses")
    group = relationship("Group", backref="courses")
    semester = relationship("Semester", backref="courses")


class Exam(Base):
    __tablename__ = "exam"
    id = Column(Integer, primary_key=True)
    exam_date = Column(Date)
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("Course", backref="exams")


class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    date = Column(Date)
    exam_id = Column(Integer, ForeignKey("exam.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    exam = relationship("Exam", backref="grades")
    student = relationship("Student", backref="grades")
    __table_args__ = (UniqueConstraint("exam_id", "student_id"),)


class Building(Base):
    __tablename__ = "building"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Classroom(Base):
    __tablename__ = "classroom"
    id = Column(Integer, primary_key=True)
    number = Column(String(50))
    building_id = Column(Integer, ForeignKey("building.id"))
    building = relationship("Building", backref="classrooms")


class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True)
    day_of_week = Column(String(50))
    start_time = Column(Time)
    end_time = Column(Time)
    group_id = Column(Integer, ForeignKey("group_.id"))
    classroom_id = Column(Integer, ForeignKey("classroom.id"))
    group = relationship("Group", backref="schedules")
    classroom = relationship("Classroom", backref="schedules")


class CourseProgram(Base):
    __tablename__ = "courseprogram"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("Course", backref="course_programs")


class Curriculum(Base):
    __tablename__ = "curriculum"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    faculty_id = Column(Integer, ForeignKey("faculty.id"))
    course_id = Column(Integer, ForeignKey("course.id"))
    faculty = relationship("Faculty", backref="curricula")
    course = relationship("Course", backref="curricula")


class Assignment(Base):
    __tablename__ = "assignment"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    date = Column(Date)
    description = Column(String)
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("Course", backref="assignments")


class Homework(Base):
    __tablename__ = "homework"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    date = Column(Date)
    description = Column(String)
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("Course", backref="homeworks")


class AssignmentTeacher(Base):
    __tablename__ = "assignmentteacher"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"))
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    assignment = relationship("Assignment", backref="assignment_teachers")
    teacher = relationship("Teacher", backref="assigned_assignments")


class HomeworkTeacher(Base):
    __tablename__ = "homeworkteacher"
    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey("homework.id"))
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    homework = relationship("Homework", backref="homework_teachers")
    teacher = relationship("Teacher", backref="assigned_homeworks")


class AssignmentGrade(Base):
    __tablename__ = "assignmentgrade"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    grade = Column(Integer)
    assignment = relationship("Assignment", backref="assignment_grades")
    student = relationship("Student", backref="assignment_grades")
    __table_args__ = (UniqueConstraint("assignment_id", "student_id"),)


class HomeworkGrade(Base):
    __tablename__ = "homeworkgrade"
    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey("homework.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    grade = Column(Integer)
    homework = relationship("Homework", backref="homework_grades")
    student = relationship("Student", backref="homework_grades")
    __table_args__ = (UniqueConstraint("homework_id", "student_id"),)

