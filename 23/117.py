

def f(x,l):
    if l==0:
        n.add(x)
        return
    return f(x+1,l-1),f(x+5,l-1),f(x*3,l-1)

n=set()
f(1,7)
print(len(n))