from sys import*
setrecursionlimit(20000)

def f(n):
    return 3*g(n-3)+7


def g(n):
    if n<=20: return n+2
    else: return g(n-3)+1

print(f(37811))