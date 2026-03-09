from functools import*
from sys import*
setrecursionlimit(2000000)
@lru_cache(None)

def f(x,n):
    x=bin(int(x))[2:]

    if x==n: return 1
    if int(x,2)<int(n,2): return 0
    return f(int(x,2)-1,n)+f(int(str(x)[:-1],2),n)


print(f(55,'110'))