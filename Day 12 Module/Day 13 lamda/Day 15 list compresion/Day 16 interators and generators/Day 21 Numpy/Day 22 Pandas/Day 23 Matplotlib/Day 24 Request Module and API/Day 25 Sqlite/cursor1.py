import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTERGER)      
""")
cursor.execute("INSERT INTO students (name,age)VALUES(?,?)",("Harshad", 22)
               )
conn.commit()
print("1 Record Inserted Succesfully")
conn.close()