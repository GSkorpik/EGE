from sys import*
setrecursionlimit(20000)

def f(n):

    if n>=110000:
        return 4+n
    else:
        return (n+7)*f(n+12)

print((f(113)+f(137))/(2*f(149)))