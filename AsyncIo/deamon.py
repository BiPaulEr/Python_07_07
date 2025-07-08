from threading import Thread
import time
import threading
def simple_worker(caractere):
    #print(threading.current_thread())
    for i in range(0, 10):
        print(caractere, end= '', flush=True)
        time.sleep(2)
    
def info(t1):
    print(t1.name)
    print(t1.ident)
    print(t1.is_alive())
    
t1 = Thread(target=simple_worker, daemon = False, args=("*"))
t1.start()

t2 = Thread(target=simple_worker, daemon = True, args=("+"))
t2.start()

#print(threading.current_thread())
#t1.join()

t3 = Thread(target=simple_worker, daemon = True, args=("^"))
t3.start()