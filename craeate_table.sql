CREATE TABLE Semester (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100)
);

CREATE TABLE Faculty (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100)
);

CREATE TABLE Group_ (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100),
  "faculty_id" INT,
  FOREIGN KEY ("faculty_id") REFERENCES Faculty ("id")
);

CREATE TABLE Student (
  "id" SERIAL PRIMARY KEY,
  "first_name" VARCHAR(50),
  "last_name" VARCHAR(50),
  "date_of_birth" DATE,
  "group_id" INT,
  FOREIGN KEY ("group_id") REFERENCES Group_ ("id")
);

CREATE TABLE Department (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100),
  "faculty_id" INT,
  FOREIGN KEY ("faculty_id") REFERENCES Faculty ("id")
);

CREATE TABLE Teacher (
  "id" SERIAL PRIMARY KEY,
  "first_name" VARCHAR(50),
  "last_name" VARCHAR(50),
  "date_of_birth" DATE,
  "department_id" INT,
  FOREIGN KEY ("department_id") REFERENCES Department ("id")
);

CREATE TABLE Course (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100),
  "teacher_id" INT,
  "group_id" INT,
  "semester_id" INT,
  FOREIGN KEY ("teacher_id") REFERENCES Teacher ("id"),
  FOREIGN KEY ("group_id") REFERENCES Group_ ("id"),
  FOREIGN KEY ("semester_id") REFERENCES Semester ("id")
);

CREATE TABLE Exam (
  "id" SERIAL PRIMARY KEY,
  "exam_date" DATE,
  "course_id" INT,
  FOREIGN KEY ("course_id") REFERENCES Course ("id")
);

CREATE TABLE Grade (
  "id" SERIAL PRIMARY KEY,
  "value" INT,
  "date" DATE,
  "exam_id" INT,
  "student_id" INT,
  FOREIGN KEY ("exam_id") REFERENCES Exam ("id"),
  FOREIGN KEY ("student_id") REFERENCES Student ("id"),
  CONSTRAINT unique_exam_student UNIQUE ("exam_id", "student_id")
);


CREATE TABLE Building (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(100)
);

CREATE TABLE Classroom (
  "id" SERIAL PRIMARY KEY,
  "number" VARCHAR(50),
  "building_id" INT,
  FOREIGN KEY ("building_id") REFERENCES Building ("id")
);

CREATE TABLE Schedule (
  "id" SERIAL PRIMARY KEY,
  "day_of_week" VARCHAR(50),
  "start_time" TIME,
  "end_time" TIME,
  "group_id" INT,
  "classroom_id" INT,
  FOREIGN KEY ("group_id") REFERENCES Group_ ("id"),
  FOREIGN KEY ("classroom_id") REFERENCES Classroom ("id")
);

CREATE TABLE CourseProgram (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100),
  "course_id" INT,
  FOREIGN KEY ("course_id") REFERENCES Course ("id")
);

CREATE TABLE Curriculum (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100),
  "faculty_id" INT,
  "course_id" INT,
  FOREIGN KEY ("faculty_id") REFERENCES Faculty ("id"),
  FOREIGN KEY ("course_id") REFERENCES Course ("id")
);

CREATE TABLE Assignment (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100),
  "date" DATE,
  "description" TEXT,
  "course_id" INT,
  FOREIGN KEY ("course_id") REFERENCES Course ("id")
);

CREATE TABLE Homework (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(100),
  "date" DATE,
  "description" TEXT,
  "course_id" INT,
  FOREIGN KEY ("course_id") REFERENCES Course ("id")
);

CREATE TABLE AssignmentTeacher (
  "id" SERIAL PRIMARY KEY,
  "assignment_id" INT,
  "teacher_id" INT,
  FOREIGN KEY ("assignment_id") REFERENCES Assignment ("id"),
  FOREIGN KEY ("teacher_id") REFERENCES Teacher ("id")
);

CREATE TABLE HomeworkTeacher (
  "id" SERIAL PRIMARY KEY,
  "homework_id" INT,
  "teacher_id" INT,
  FOREIGN KEY ("homework_id") REFERENCES Homework ("id"),
  FOREIGN KEY ("teacher_id") REFERENCES Teacher ("id")
);

CREATE TABLE AssignmentGrade (
  "id" SERIAL PRIMARY KEY,
  "assignment_id" INT,
  "student_id" INT,
  "grade" INT,
  FOREIGN KEY ("assignment_id") REFERENCES Assignment ("id"),
  FOREIGN KEY ("student_id") REFERENCES Student ("id"),
  CONSTRAINT unique_assignment_student UNIQUE ("assignment_id", "student_id")
);

CREATE TABLE HomeworkGrade (
  "id" SERIAL PRIMARY KEY,
  "homework_id" INT,
  "student_id" INT,
  "grade" INT,
  FOREIGN KEY ("homework_id") REFERENCES Homework ("id"),
  FOREIGN KEY ("student_id") REFERENCES Student ("id"),
  CONSTRAINT unique_homework_student UNIQUE ("homework_id", "student_id")
);
