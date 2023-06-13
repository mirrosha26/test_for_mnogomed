-- Выбрать всех студентов, обучающихся на курсе "Математика".
SELECT ( st.first_name || ' ' || st.last_name ) AS "Cтудентов с курса 'Математика'" FROM group_ as gr
JOIN course ON course.group_id = gr.id
JOIN student AS st ON st.group_id = gr.id
WHERE Course.title LIKE 'Математика';

-- Обновить оценку студента по курсу.
CREATE OR REPLACE PROCEDURE update_grade(st_id integer, new_grade integer, c_id integer)
LANGUAGE SQL
AS $$
UPDATE grade
SET value = new_grade
FROM exam
JOIN course ON course.id = exam.course_id
WHERE grade.exam_id = exam.id
  AND exam.course_id = c_id
  AND grade.student_id = st_id;
$$;

CALL update_grade(1, 100, 1);  

--- Выбрать всех преподавателей, которые преподают в здании №3.
SELECT ( teacher.first_name || ' ' || teacher.last_name ) AS "Преподователи здания №3"
FROM homeworkteacher
JOIN teacher ON teacher.id = homeworkteacher.teacher_id
JOIN homework ON homework.id = homeworkteacher.homework_id
WHERE homework.title LIKE 'Задание 3';


-- Удалить задание для самостоятельной работы, которое было создано более года назад.
DELETE FROM assignmentGrade
WHERE assignment_id IN (
  SELECT id
  FROM Assignment
  WHERE date < CURRENT_DATE - INTERVAL '1 year'
);

DELETE FROM assignmentteacher
WHERE assignment_id IN (
  SELECT id
  FROM Assignment
  WHERE date < CURRENT_DATE - INTERVAL '1 year'
);

DELETE FROM Assignment
WHERE date < CURRENT_DATE - INTERVAL '1 year';


--Добавить новый семестр в учебный год.
INSERT INTO semester (title)
VALUES ('Осенний семестр 2023');