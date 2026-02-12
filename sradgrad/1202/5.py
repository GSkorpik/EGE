def f(n):
    s=''
    while n!=0:
        a=n%3
        s=str(a)+s
        n//=3
    return s
a=set()
for n in range(1,1000):
    t=f(n)
    if n%3==0:
        r=t+t[-2:]
    else:
        st=sum(map(int,t))
        r=t+str(f(st*3))
    r=int(r,3)

    if 800<r<850:
        a.add(r)
print(a)