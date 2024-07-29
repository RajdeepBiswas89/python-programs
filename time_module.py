import time
def usingforloop():
    for i in range(100):
        print(i)
def usingwhileloop():
    i=0
    while i<100:
        i=i+1
        print(i)
init=time.time()
usingforloop()
t1= time.time()-1
init=time.time()
usingwhileloop()
t2= time.time() -1
print("time taken for FOR loop",t1)
print("time taken for while loop",t2)

