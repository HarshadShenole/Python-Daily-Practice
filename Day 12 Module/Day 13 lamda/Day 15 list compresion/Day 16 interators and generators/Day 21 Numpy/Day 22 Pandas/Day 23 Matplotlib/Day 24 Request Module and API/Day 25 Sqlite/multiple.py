import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER)    
 """)
#MULTIPLE RECORDS ADD
students = [
    ("Harshad",22),
    ("Amit",21),
    ("Rahul", 23),
    ("Sneha", 22),
    ("shreya",22)
]
cursor.executemany(
    "INSERT INTO students(name,age)VALUES(?,?)",students
)
conn.commit()
print("5 Records Inserted Succesfully")
conn.close()