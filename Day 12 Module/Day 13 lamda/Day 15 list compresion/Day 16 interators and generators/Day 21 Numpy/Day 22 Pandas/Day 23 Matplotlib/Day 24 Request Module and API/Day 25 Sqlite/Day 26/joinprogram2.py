import threading

def task():         #create a function
    print("Threading Running")
t = threading.Thread(target=task) #Create a thread

t.start()
t.join()
print("Main Thread Finished")