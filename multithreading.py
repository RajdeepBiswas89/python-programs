import threading
import time
def mytime(secs):
    print(f"sleeping for {secs}")
    time.sleep(secs)
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

#after writing join function it will take max time from the given time
t1.join()
t2.join()
t3.join()
time2=time.perf_counter()
print(time2-time1)