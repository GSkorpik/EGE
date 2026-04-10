from sys import*
setrecursionlimit(20000)
def f(n):
    if n>29999: return n+f(n-5)
    if n<30000: return n+g(n-2)

def g(n):
    if n<30000: return 10+n+g(n+3)
    if n>29999: return n**2

print(f(75000))



