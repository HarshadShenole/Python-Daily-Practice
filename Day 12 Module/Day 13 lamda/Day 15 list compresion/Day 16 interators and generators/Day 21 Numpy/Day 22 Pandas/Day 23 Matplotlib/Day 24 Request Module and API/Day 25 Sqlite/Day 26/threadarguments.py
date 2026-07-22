import threading
def hello():
    print("Hello Github")

t1 = threading.Thread(target=hello)

t1.start()
t1.join()