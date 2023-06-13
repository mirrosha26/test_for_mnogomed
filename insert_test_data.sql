INSERT INTO Semester ("title")
VALUES
  ('Осенний семестр'),
  ('Весенний семестр');

INSERT INTO Faculty ("title")
VALUES
  ('Факультет информационных технологий'),
  ('Факультет гуманитарных наук');

INSERT INTO Group_ ("title", "faculty_id")
VALUES
  ('Группа ИТ-1', 1),
  ('Группа ГН-1', 2);

INSERT INTO Student ("first_name", "last_name", "date_of_birth", "group_id")
VALUES
  ('Иван', 'Иванов', '2000-01-01', 1),
  ('Екатерина', 'Смирнова', '1999-05-15', 2),
  ('Алексей', 'Петров', '2001-08-20', 1),
  ('Мария', 'Сидорова', '2002-03-10', 1),
  ('Александр', 'Ковалев', '2003-07-25', 2),
  ('Елена', 'Петрова', '2001-11-05', 1);

INSERT INTO Department ("title", "faculty_id")
VALUES
  ('Кафедра программной инженерии', 1),
  ('Кафедра истории искусств', 2);

INSERT INTO Teacher ("first_name", "last_name", "date_of_birth", "department_id")
VALUES
  ('Андрей', 'Смирнов', '1980-06-10', 1),
  ('Мария', 'Ковалева', '1975-03-18', 2),
  ('Иван', 'Петров', '1985-09-05', 1),
  ('Елена', 'Иванова', '1983-12-25', 2);

INSERT INTO Course ("title", "teacher_id", "group_id", "semester_id")
VALUES
  ('Программирование', 1, 1, 1),
  ('Искусство Древней Греции', 2, 2, 2),
  ('Математика', 3, 1, 1),
  ('Литература', 4, 2, 2);

INSERT INTO Exam ("exam_date", "course_id")
VALUES
  ('2023-12-15', 1),
  ('2023-05-30', 2),
  ('2023-12-20', 3),
  ('2023-06-10', 4);

INSERT INTO Grade ("value", "date", "exam_id", "student_id")
VALUES
  (85, '2023-12-15', 1, 1),
  (92, '2023-05-30', 2, 2),
  (78, '2023-12-20', 3, 3),
  (90, '2023-06-10', 4, 4);

INSERT INTO Building ("name")
VALUES
  ('Главный корпус'),
  ('Корпус гуманитарных наук');

INSERT INTO Classroom ("number", "building_id")
VALUES
  ('101', 1),
  ('202', 2);

INSERT INTO Schedule ("day_of_week", "start_time", "end_time", "group_id", "classroom_id")
VALUES
  ('Понедельник', '08:00:00', '10:00:00', 1, 1),
  ('Вторник', '13:00:00', '15:00:00', 2, 2);

INSERT INTO CourseProgram ("title", "course_id")
VALUES
  ('Структуры данных', 1),
  ('История искусства XX века', 2);

INSERT INTO Curriculum ("title", "faculty_id", "course_id")
VALUES
  ('Бакалавриат ИТ', 1, 1),
  ('Бакалавриат истории искусств', 2, 2);

INSERT INTO Assignment ("title", "description", "date", "course_id")
VALUES
  ('Лабораторная работа 1', 'Написать программу на языке Python', '2023-12-15', 1),
  ('Эссе 1', 'Написать эссе на тему "Искусство в Древней Греции"', '2019-12-15', 2);

INSERT INTO Homework ("title", "description", "date", "course_id")
VALUES
  ('Домашнее задание 1', 'Выполнить упражнения 1-5 из учебника', '2023-12-15', 1),
  ('Реферат', 'Написать реферат на тему "Архитектура Древней Греции"', '2020-12-15', 2),
  ('Задание 3', 'Упражнения 203, 204, 212(а, б, в)', '2023-11-11', 1);

INSERT INTO AssignmentTeacher ("assignment_id", "teacher_id")
VALUES
  (1, 1),
  (2, 2);

INSERT INTO HomeworkTeacher ("homework_id", "teacher_id")
VALUES
  (1, 3),
  (2, 2),
  (3, 3),
  (3, 4);

INSERT INTO AssignmentGrade ("assignment_id", "student_id", "grade")
VALUES
  (1, 1, 90),
  (2, 2, 95);

INSERT INTO HomeworkGrade ("homework_id", "student_id", "grade")
VALUES
  (1, 1, 80),
  (2, 2, 85);