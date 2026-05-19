def f(x,n):
    if x==n: return 1
    if x>n: return 0
    if ((x%100-x%10)//10)<(x%10):
        b=str(x)
        return f(x+1,n)+f(int(b[0]+b[-1]+b[-2]),n)
    return f(x+1,n)

print(f(101,154))