

def fuba(f1,f2,n):
    if n==2: return f2
    fu=f1+f2
    f1=f2
    f2=fu
    return fuba(f1,f2,n-1)

def f(x,n):
    if x==n: return 1
    if x>n: return 0
    return f(x+1,n)+f(x+3,n)+f(fuba(1,1,x),n)

print(f(6,21))
