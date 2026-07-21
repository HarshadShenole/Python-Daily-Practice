import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM students  WHERE NAME=?",("rahul",))
print("Data is Deleted")
conn.commit()
conn.close()
