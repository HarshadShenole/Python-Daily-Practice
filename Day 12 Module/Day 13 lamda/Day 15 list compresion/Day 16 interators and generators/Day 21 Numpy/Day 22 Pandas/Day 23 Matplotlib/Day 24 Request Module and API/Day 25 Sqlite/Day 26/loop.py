import threading

def numbers():
    for i in range(1,6):
        print(i)

def letters():
    for ch in "ABCD":
        print(ch)
t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed")