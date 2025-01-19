

from functools import *
@lru_cache(None)
def F(n):
    if n<=3:
        return n
    if n % 2 == 0 :
        return F(n - 1) + 2 * F(n // 2)
    return F(n - 1) + F(n - 3)
n= 1
k= 0

while F(n)<10**8:
    k+=1
    print(k,n,F(n))
    n=+1
print(k)