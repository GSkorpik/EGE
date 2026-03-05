

def f(x,l,n):

    if l==0:
        if x==n: return 1
        return 0
    return f(x+1,l-1,n)+f(x+3,l-1,n)+f(x*2,l-1,n)



print(f(2,7,25))