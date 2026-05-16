from sys import*
setrecursionlimit(20000000)

def f(n):
    if n>=14: return n*f(n-1)
    else: return 8*g(n-3)


def g(n):
    if n<31: return 4
    else:
        return n//2*g(n-2)

print(f(320726)//g(641450))