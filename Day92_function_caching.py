import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print('DONE FOR 20')
print(fx(2))
print('done for 2')