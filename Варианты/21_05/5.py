def f(n):
    s=''
    while n!=0:
        a=n%3
        s=str(a)+s
        n//=3
    return s


for n in range(1,1000):
    t=f(n)
    if n%3==0:
        r='1'+t+'02'
    else:
        t1=(n%3)*5
        r=t+f(t1)

    r=int(r,3)
    if r>=177:
        print(n)
        break