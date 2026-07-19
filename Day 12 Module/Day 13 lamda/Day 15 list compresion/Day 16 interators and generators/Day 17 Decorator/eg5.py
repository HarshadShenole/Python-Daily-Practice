def login(func):
    def wrapper():
        print("Checking Login....")
        func()
    return wrapper

login
def profile():
    print("Profile Opened")

profile()