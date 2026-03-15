def f(x,n):
    if x==n: return 1
    if x<n: return 0
    return f(x-1,n)+f(x//2,n)

print(f(40,17)*f(17,6))