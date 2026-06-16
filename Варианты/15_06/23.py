def f(x,n):
    if x==n:return 1
    if x>n: return 0
    return f(x+2,n)+f(x+3,n)+f(x*2,n)




print(f(7,14)*f(14,32)+f(7,21)*f(21,32)-f(7,14)*f(14,21)*f(21,32))