def f(x,n):
    if x==n: return 1
    if x<n or x==9: return 0
    return f(x-1,n)+f(x-3,n)+f(x//3,n)

print(f(21,12)*f(12,3))