import threading
import time
from concurrent.futures import ThreadPoolExecutor
def mytime(secs):
    print(f"sleeping for {secs}")
    time.sleep(secs)
    return secs
time1=time.perf_counter()
#normal code
# mytime(4)
# mytime(2)
# mytime(1)
t1=threading.Thread(target=mytime, args=[4])# creating a new thread
t2=threading.Thread(target=mytime,args=[2])
t3=threading.Thread(target=mytime,args=[1])
t1.start()
t2.start()
t3.start()
def mypolling():
  with ThreadPoolExecutor() as executor:
    future1 = executor.submit(mytime,4)
    future2 =executor.submit(mytime,3)
    future3 = executor.submit(mytime,2)
#using map function for a larger set of numbers
    lists1=[2,4,6,7,7,8]
    i =executor.map(mytime,lists1)
    for i in lists1:
       print(i)


    print(future1.result())
    print(future2.result())
    print(future3.result())
mypolling()