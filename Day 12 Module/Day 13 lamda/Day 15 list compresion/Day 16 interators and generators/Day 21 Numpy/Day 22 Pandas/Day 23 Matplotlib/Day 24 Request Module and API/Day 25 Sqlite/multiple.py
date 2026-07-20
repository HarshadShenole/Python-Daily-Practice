import sqlite3
conn = sqlite3.connect("studentS.db")
cursor = conn.cursor()
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS students(
               id INTERGER,
               name TEXT,
               AGE INTEGER
               )    

""")
#multiple student 
students = [
    ("Harshad",22),
    ("Amit",21),
    ("Rahul",20),
    ("Priya",23)
]
#Insert multiple records 
cursor.executemany(
    "INSERT INTO students(name,age)VALUES(?,?)",
    students
)
conn.close()
print("4 records Inserted Succesfully!")
#Close the database connection
conn.close()