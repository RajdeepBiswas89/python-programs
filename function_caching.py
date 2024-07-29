from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
print(fx(20))
print("done for 20")
print(fx(10))
print("done for 10")
print(fx(5))
print('done for 5')
#after this it will store in the cache memory 
 
print(fx(20))
print("done for 20")
print(fx(10))
print("done for 10")
print(fx(5))
print('done for 5')