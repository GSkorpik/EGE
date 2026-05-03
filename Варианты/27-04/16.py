from functools import lru_cache
@lru_cache()

def f(n):
    if n==0: return 0
    elif n>0 and n%2!=0:
        return f(n//10)+(n%10)
    elif n>0 and n%2==0: return f(n//10)

k=0
for n in range(10**9,6*10**9+1):
    if f(n)==1:
        k+=1
print(k)

