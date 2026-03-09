
def f(x,l):
    if l==0:
        n.add(x)
        return
    f(x - 1, l - 1)
    f(x - 2, l - 1)

    if round(x**0.5)**2==x and x>=0:
        f(round(x**0.5),l-1)

n=set()
f(133,17)
print(len(n))