

def f(x,l):
    if l==0:
        if x==22:
            return 1
        return 0
    return f(x+1,l-1)+f(x+2,l-1)+f(x+3,l-1)

print(f(3,7))