def border(func):
    def wrapper():
        print("********")
        func()
        print("********")

    return wrapper
@border
def name():
    print("Harhad")

name()