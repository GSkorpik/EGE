
def f(x,n):
    if x==n: return 1
    if x>n or x ==8: return 0
    else:
        return f(x+1,n)+f(x+4,n)+f(x*4,n)

print(f(2,6)*f(6,24))