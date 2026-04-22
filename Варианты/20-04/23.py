

def f(x,n):
    if x==n: return 1
    if x>n or x==11 or x==8: return 0
    else:
        return f(x+1,n)+f(x+2,n)+f(x*3,n)


print(f(2,5)*f(5,21))