from sys import*

setrecursionlimit(1000000000)

def f(n):
    if n<220: return n
    else: return (n-3)*f(n-4)

print((f(123817)-f(123813))//(9*f(123809)))