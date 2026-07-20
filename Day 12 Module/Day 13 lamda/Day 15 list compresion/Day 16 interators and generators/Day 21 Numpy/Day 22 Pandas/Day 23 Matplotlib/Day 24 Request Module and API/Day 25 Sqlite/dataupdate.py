import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute (
    "UPDATE students SET age =? WHERE name=?",
       (23, "Harshad") 
       )

conn.commit()
print("Data is Updated")