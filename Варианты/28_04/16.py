from sys import*
from math import*

setrecursionlimit(2000000)


def f(a,b):
    if b==0: return a
    if a>=b>0: return f(a-b,b)
    if a<b: return f(b,a)

k=0
for n in range(10**8,2*10**8+1):
    if gcd(n,105)==1:
        k+=1


print(k)