USERNAME = "admin"
PASSWORD = "1234"

def login():
    username = input("Enter Username :")

    password = input("Enter Password: ")


    if username == USERNAME and password == PASSWORD :
     print("Login Successful")
     return True

    else:
       print("Invalid username or Passowrd")
       return False 