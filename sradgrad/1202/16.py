from sys import*
setrecursionlimit(200000)

def f(n):
    if n>=20:
        return f(n-4)+4620
    else:
        return 8*(g(n-12)-21)

def g(n):
    if n>=384242:
        return n/4+18
    else:
        return 12+g(n+41)

print(f(913))