from sys import*
setrecursionlimit(200000)

def f(n):
    if n<5: return 11
    else:
        return 11*f(n-6)


print(f(41387)/11**6897)