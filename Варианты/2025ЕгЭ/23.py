
def f(x,n):
    if x==n:
        return 1
    if x<n or x==13: return 0
    else:
        return f(x-1,n)+f(x-2,n)+f(x//3,n)
print(f(19,6)*f(6,4))