def welcome(func):
    def wrapper():
        print("Welcome")
        func()

    return wrapper
@welcome
def student():
    print("Harshad")

student()