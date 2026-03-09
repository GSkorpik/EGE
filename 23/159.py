from sys import*
setrecursionlimit(20000)

def fo(x):
    fuba = [1, 1, 2, 3, 5, 8, 13, 21]
    for i in range(0,8):
        if x<=fuba[i]:
            k=i-1
            return fuba[k]



def f(x,n):
    if x==n: return 1
    if x>n: return 0
    return f(x+1,n)+f(x+4,n)+f(x+fo(x),n)



print(f(2,16))

