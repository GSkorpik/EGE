from sys import*
setrecursionlimit(100000)

def f(n):
    if n<=10: return n
    else: return n-7+f(n-21)


print((f(185734)-f(185650))//f(40))