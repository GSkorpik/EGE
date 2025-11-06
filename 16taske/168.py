'''def F(n):
    a=[0,1, 2]
    for i in range(3,n+1):
        a.append(i+a[i-2])
    return a[n]
print(F(2023)+F(2020))

'''
from sys import*
setrecursionlimit(2000)

def f(n):
    if n<=2: return n
    else:
        return n+f(n-2)

print(f(2023)+f(2020))