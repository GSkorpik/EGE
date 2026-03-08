
def f(x,n,l):
    if x==n:
        return l
    if x>n: return 10**10
    if x<n: return min(f(x+1,n,l+1),f(x+2,n,l+1),f(x*2,n,l+1))

print(f(1,28,0))