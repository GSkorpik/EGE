
def f(x,n,k):
    if x==n: return 1
    if x>n: return 0
    if k==1: return f(x*2,n,0)+f(x+1,n,0)
    return f(x+1,n,0)+f(x+2,n,1)+f(x*2,n,0)

print(f(1,12,0))