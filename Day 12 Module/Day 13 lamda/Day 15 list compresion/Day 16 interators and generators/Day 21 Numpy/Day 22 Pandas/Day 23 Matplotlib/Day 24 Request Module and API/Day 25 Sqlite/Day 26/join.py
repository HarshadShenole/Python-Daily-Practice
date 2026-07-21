import threading
def hello():
    print("Hello")

t1 = threading.Thread(target = hello)

t1.start()
t1.join()

print("Program End")