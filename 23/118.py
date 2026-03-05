from functools import*
from sys import*
setrecursionlimit(200000)
@lru_cache(None)


def f(x,l,y):
    if x>y: return
    if l==6 and x==y:
        c.add(x)
        return

    return f(x+1,l+1,y),f(x+2,l+1,y),f(x*2,l+1,y)

c=set()
for y in range(34,60):
    f(1,0,y)

print(len(c))