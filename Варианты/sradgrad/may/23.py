def f(x,n):
    if x==n: return 1
    if x>n: return 0
    return f(x+3,n)+f(x+4,n)+f(x**2,n)


print(f(4,7)*f(7,18)*f(18,41))