import threading #import thread class

class thread_class(threading.Thread):  #including threading.Thread class to class thread_class
    def run(self):
        for _ in range(120):
            print(threading.current_thread().getName())
            
x = thread_class(name = "Thread 1 is called out")  
y = thread_class(name = "Thread 2 is called out")
x.start()
y.start()