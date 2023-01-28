import time
from functools import lru_cache

@lru_cache(maxsize= 6)
def somework(n):
    time.sleep(3)
    return n

if __name__ == '__main__':
    print("now running function")
    somework(4)
    print("again running")
    somework(8)
    print("after 8")
    somework(9)
    print("after 9")
    somework(5)
    print("after 5")
    somework(5)
    print("after 5")
    somework(6)
    print("after 6")
    somework(7)
    print("done")