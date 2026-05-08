from sys import*
setrecursionlimit(200000)

def f(n):
    if n<=2: return 5
    else:
        return f(n-2)+n

print(f(23023))