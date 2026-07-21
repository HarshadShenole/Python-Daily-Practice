import threading
def first():
    print("First Thread")

def second():
    print("Second Thread")

t1 = threading.Thread(target=first)
t2 = threading.Thread(target=second)

t1.start()
t2.start()

print("Completed")