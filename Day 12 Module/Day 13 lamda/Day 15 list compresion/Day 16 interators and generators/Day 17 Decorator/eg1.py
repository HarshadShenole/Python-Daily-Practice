def decorator(func):
    def wrapper():
        print("Program Started")

        func()

        print("Program Ended")

    return wrapper 
@decorator
def hello():
    print("Hello")

hello()