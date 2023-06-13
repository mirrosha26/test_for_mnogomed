# Задание для кандидата на должность Junior Python Developer

Целью этого задания является разработка структуры базы данных и реализация API для "Системы управления университетом". Эта система предназначена для учета студентов, преподавателей, курсов, групп, отделений университета, оценок и других соответствующих данных.

## Часть 1: База данных

### 1. ER-диаграмма и описание сущностей

![ER-диаграмма](/New_University.png)

#### Описание сущностей

1. Semester (Семестр): Содержит информацию о семестре, включая поля "id" и "title".
2. Faculty (Факультет): Содержит информацию о факультете, включая поля "id" и "title".
3. Group_ (Группа): Содержит информацию о группе, включая поля "id", "title" и "faculty_id", где "faculty_id" является внешним ключом, связывающим группу с факультетом.
4. Student (Студент): Содержит информацию о студенте, включая поля "id", "first_name", "last_name", "date_of_birth" и "group_id", где "group_id" является внешним ключом, связывающим студента с группой.
5. Department (Кафедра): Содержит информацию о кафедре, включая поля "id", "title" и "faculty_id", где "faculty_id" является внешним ключом, связывающим кафедру с факультетом.
6. Teacher (Преподаватель): Содержит информацию о преподавателе, включая поля "id", "first_name", "last_name", "date_of_birth" и "department_id", где "department_id" является внешним ключом, связывающим преподавателя с кафедрой.
7. Course (Курс): Содержит информацию о курсе, включая поля "id", "title", "teacher_id", "group_id" и "semester_id", где "teacher_id", "group_id" и "semester_id" являются внешними ключами, связывающими курс с преподавателем, группой и семестром соответственно.
8. Exam (Экзамен): Содержит информацию об экзамене, включая поля "id", "exam_date" и "course_id", где "course_id" является внешним ключом, связывающим экзамен с курсом.
9. Grade (Оценка): Содержит информацию об оценке, включая поля "id", "value", "date", "exam_id" и "student_id

", где "exam_id" и "student_id" являются внешними ключами, связывающими оценку с экзаменом и студентом соответственно.
10. Building (Здание): Содержит информацию о здании, включая поля "id" и "name".
11. Classroom (Аудитория): Содержит информацию об аудитории, включая поля "id", "number" и "building_id", где "building_id" является внешним ключом, связывающим аудиторию с зданием.
12. Schedule (Расписание): Содержит информацию о расписании, включая поля "id", "day_of_week", "start_time", "end_time", "group_id" и "classroom_id", где "group_id" и "classroom_id" являются внешними ключами, связывающими расписание с группой и аудиторией соответственно.
13. CourseProgram (Учебная программа): Содержит информацию об учебной программе, включая поля "id", "title" и "course_id", где "course_id" является внешним ключом, связывающим учебную программу с курсом. Поле "id" также может использоваться как ключ для URL, содержащего ссылку на саму программу (например, `f'{base_url}/courseprogram/{id}'`).
14. Curriculum (Учебный план): Содержит информацию об учебном плане, включая поля "id", "title", "faculty_id" и "course_id", где "faculty_id" и "course_id" являются внешними ключами, связывающими учебный план с факультетом и курсом соответственно. Поле "id" можно использовать в URL для хранения ссылки на учебный план (например, `f'{base_url}/curriculum/{id}'`).
15. Assignment (Задание): Содержит информацию о задании, включая поля "id", "title", "date", "description" и "course_id", где "course_id" является внешним ключом, связывающим задание с курсом.
16. Homework (Домашнее задание): Содержит информацию о домашнем задании, включая поля "id", "title", "date", "description" и "course_id", где "course_id" является внешним ключом, связывающим домашнее задание с курсом.
17. AssignmentTeacher (Задание - Преподаватель): Связующая таблица для отношения "многие ко многим" между заданиями и преподавателями. Содержит поля "assignment_id" и "teacher_id", которые являются внешними

 ключами, связывающими задание и преподавателя.
18. HomeworkTeacher (Домашнее задание - Преподаватель): Связующая таблица для отношения "многие ко многим" между домашними заданиями и преподавателями. Содержит поля "homework_id" и "teacher_id", которые являются внешними ключами, связывающими домашнее задание и преподавателя.
19. AssignmentGrade (Оценка за задание): Содержит информацию об оценке за задание, включая поля "id", "assignment_id", "student_id" и "grade", где "assignment_id" и "student_id" являются внешними ключами, связывающими оценку с заданием и студентом соответственно.
20. HomeworkGrade (Оценка за домашнее задание): Содержит информацию об оценке за домашнее задание, включая поля "id", "homework_id", "student_id" и "grade", где "homework_id" и "student_id" являются внешними ключами, связывающими оценку с домашним заданием и студентом соответственно.

### Создание таблиц
[SQL скрипт](/craeate_table.sql) создает все таблицы со всеми полями, типами данных, ключами и связями.

### Заполнение таблицы тестовыми данными
[SQL скрипт](/insert_test_data.sql) заполняет таблицы тестовыми данными.

### Часть 2: SQL запросы
[SQL запросы с комментариями](/script.sql).

### Часть 3: FastAPI
[Ссылка](/university_app/) на проект.