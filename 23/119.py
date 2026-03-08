from functools import*
from sys import*
setrecursionlimit(200000)
@lru_cache(None)

def f(x,l,n):
    if x>n: return
    if l==8 and  x==n:
        c.add(x)
        return

    return f(x+1,l+1,n),f(x+3,l+1,n),f(x*3,l+1,n)

c=set()
for n in range(1000,1025):
    f(1,0,n)
print(len(c))