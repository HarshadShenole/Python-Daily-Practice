import sqlite3
conn = sqlite3.connect("Student.db")
cursor = conn.cursor()
cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS studentS(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER
               )       """)
cursor.execute(" INSERT INTO  students(name,age)VALUES(?,?)",("Harshad", 22))
conn.commit()
print("1 record Inserted Succesfully")
conn.close()