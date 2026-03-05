def f(x,n):
    if x==n: return 1
    if x>n or x==22: return 0
    if x<n: return f(x+1,n) + f(x*2,n)

print(f(5,8)*f(8,60))