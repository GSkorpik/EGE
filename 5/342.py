def f(n):
    a='0123456789abcde'
    if n<15:
        return a[n]
    else:
        return f(n//15)+a[n%15]
a=[]
for n in range(14,1000):
    b=f(n)
    if n//15==0:
        r=b+b[:2]
    else:
        c=f(n%15*13)
        r=b+c
    r=int(r,15)
    if r >700:

        a.append(r)
print(min(a))