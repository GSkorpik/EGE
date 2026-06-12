def f(x,n):
    if x==n: return 1
    if x>n: return 0
    if ((x%100-x%10)//10)<(x%10):
        t=str(x)
        t=t[:-2]+t[-1]+t[-2]
        return f(int(t),n)+f(int(x)+2,n)
    return f(x+2,n)

print(f(211,221)*f(221,256))