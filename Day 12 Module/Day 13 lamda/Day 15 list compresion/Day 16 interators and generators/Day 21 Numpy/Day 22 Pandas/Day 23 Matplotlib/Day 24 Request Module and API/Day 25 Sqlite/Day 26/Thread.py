import threading

def hello(): #Create a function
    print("Hello Github")

t1 = threading.Thread(target=hello)  #Create a thread

t1.start()