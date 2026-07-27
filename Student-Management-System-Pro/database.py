import sqlite3


def connect_db():
    conn = sqlite3.connect("students.db")
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        roll_no INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT,
        course TEXT,
        marks REAL
    )
    """)

    conn.commit()
    conn.close()


def add_student(student):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students
    (roll_no, name, age, email, course, marks)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        student.roll_no,
        student.name,
        student.age,
        student.email,
        student.course,
        student.marks
    ))

    conn.commit()
    conn.close()

    print("Student Added Successfully")


def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students


def search_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    conn.close()

    return student


def update_student(student):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET
        name = ?,
        age = ?,
        email = ?,
        course = ?,
        marks = ?
    WHERE roll_no = ?
    """, (
        student.name,
        student.age,
        student.email,
        student.course,
        student.marks,
        student.roll_no
    ))

    conn.commit()
    conn.close()

    print("Student Updated Successfully")


def delete_student(roll_no):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
             "DELETE FROM students WHERE roll_no = ? ",
             (roll_no,)
     )

        conn.commit()
        conn.close()

        print("student Delete Successfully")