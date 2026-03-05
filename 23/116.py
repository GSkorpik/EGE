def f(x,l):
    if  l==4:
        c.add(x)
        return
    return f(x+1,l+1),f(x+5,l+1),f(x*3,l+1)
c=set()
f(1,0)
print(len(c))
