def f(n):
    s=''
    while n!=0:
        a=n%4
        s=str(a)+s
        n//=4
    return s

m=10000
for n in range(1,100):
    s=f(n)
    if n%4==0:
        r=s+s[-2:]
    else:
        s1=sum(map(int,s))
        r=s+f(s1)

    r=int(r,4)
    if r>870 and r%2==0:
        m=min(m,r)
        print(r)
print(m,'1111111111111111')