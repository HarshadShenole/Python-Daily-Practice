import threading
def numbers():
    for i in range(10):
        print(i)

t = threading.Thread(target=numbers)
 
t.start()
t.join()