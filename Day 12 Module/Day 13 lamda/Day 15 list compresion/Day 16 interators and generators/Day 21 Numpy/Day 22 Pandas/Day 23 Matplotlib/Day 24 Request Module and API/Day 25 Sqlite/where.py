import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute(
    "SELECT * FROM students WHERE age=?",
    (22,)
)
rows = cursor.fetchall()
print(rows)