from sys import *
setrecursionlimit(100000000)
from functools import *
@lru_cache(None)

def f(x,n):
    if x==n:return 1
    if x<=10: return 0
    if x%10<(x%100-x%10)//10:
        return f(x - 2, n) + f((x % 10) * 10 + ((x % 100 - x % 10) // 10), n)
    else:
        return f(x-2,n)

print(f(57,13))