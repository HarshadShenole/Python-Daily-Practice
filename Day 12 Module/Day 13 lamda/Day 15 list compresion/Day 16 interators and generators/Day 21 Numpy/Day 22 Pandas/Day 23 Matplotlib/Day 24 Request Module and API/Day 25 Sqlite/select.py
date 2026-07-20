import sqlite3

#Connect the database 
conn = sqlite3.connect("students.db")

#Create a cursor
cursor = conn.cursor()

# Got a all data

cursor.execute("SELECT * FROM students")

# Do all rows are fectch 
rows = cursor.fetchall()

 # print the all rows 
for row in rows:
    print(row)

    # Close the connection
conn.close()

