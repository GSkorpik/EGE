def f(n):
    if n<=70: return f(n+2)+2*f(3*n)
    else: return n-50

print(f(40))
