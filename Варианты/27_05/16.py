from sys import*
setrecursionlimit(200000)

def f(n):
    if n>27:
        return 2660+f(n-4)
    else:
        return 5*(g(n-8)-41)




def g(n):
    if n<307520:
        return -2+g(n+11)
    else:
        return 32+n/30

print(f(791))