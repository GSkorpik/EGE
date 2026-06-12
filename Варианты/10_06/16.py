from sys import*
setrecursionlimit(10000000)

def f(n):
    if n>=10**7:
        return n
    else:
        return f(n+4)*(n-4)
print((996/12-73)*1000)
#print(f(1004)*(996/12-73)/f(1008))
#print((f(1000)/12-73*f(1004))/f(1008))
