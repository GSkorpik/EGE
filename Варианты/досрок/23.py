
def f(x,n):
    if x==n: return 1
    if x>n or x==7: return 0
    else:
        return f(x+1,n)+f(x+3,n)+f(x*2,n)

print(f(2,15)*f(15,25))