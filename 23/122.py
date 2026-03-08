
def f(x,n):
    if x==n:
        return 1
    if x>n: return 0
    if x<n: return f(x+2,n)+f(x+4,n)+f(x+5,n)

for n in range(33,10000):
    if f(31,n)==1001:
        print(n)
        break