from functools import*
@lru_cache(None)
def f(n,l):
    if n==227:
        L.append(l)
        return
    if n>227: return
    return f(n+1,l+1),f(n+5,l+1),f(n*3,l+1)
L=[]
f(1,0)
print(L)



'''from functools import*
@lru_cache(None)

def f(x,n,l):
    if x>n: return 10**10
    if x==n: return l
    if x<n: return min(f(x+1,n,l+1),f(x+5,n,l+1),f(x*3,n,l+1))

print(f(1,227,0))'''
