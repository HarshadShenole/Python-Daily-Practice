import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
row = cursor.fetchone()
print(row)