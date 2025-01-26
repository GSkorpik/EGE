from functools import lru_cache
@lru_cache()

def F(n):
    x=(sum(map(int,str(n))))
    if n<3:
        return 1
    if n>2 and x%2==0 :
        return F(n-1)-F(n-2)
    else:
        return F(n-1)+F(n//2)

print(F(100))