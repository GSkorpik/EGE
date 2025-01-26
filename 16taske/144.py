import sys
sys.setrecursionlimit(10000)

def F(n):
    if n>=10000:
        return n
    if n<10000 and n%2==0:
        return 1+F(n//2)
    if n < 10000 and n % 2 == 1:
        return n**2 + F(n + 2)

print(F(192)-F(9))
