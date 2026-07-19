def thanks(func):
    def wrapper():
        func()
        print("Thank You")
    return wrapper

@thanks
def shopping():
    print("shopping Done")

shopping()