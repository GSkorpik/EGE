def f(x,n):
    if x==n: return 1
    if x<n: return 0
    return f(x-8,n)+f(x//2,n)

print(f(102,43)*f(43,5))