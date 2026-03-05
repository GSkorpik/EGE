def f(x,n):
    if x==n: return 1
    if x>n: return 0
    if x<n: return f(x+1,n)+f(x+2,n)

print(f(5,10)*f(10,15))