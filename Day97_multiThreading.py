import threading
import time

# indicate some task being done
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    
time1 = time.perf_counter()
#Normal code
# func(5)
# func(3)
# func(3)

# using thread 
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func,args=[3])
t3 = threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
# calculation time
time2 = time.perf_counter()
print(time2 - time1)