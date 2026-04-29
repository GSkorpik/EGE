

def f(x,n):
    if x==n:return 1
    if x>n: return 0
    else:
        return f(x+3,n)+f(x*2,n)+f(x+2,n)

print(f(15,61)*f(61,64)*f(64,80))