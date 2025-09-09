def func(n):
    s=''
    while n!=0:
        a=n%3
        s = str(a) + s
        n//=3
    return s
a=set()
for n in range(1,1000):
    r=func(n)
    if n%3==0:
        r=r+r[-2:]
    else:
        s=sum(map(int,r))
        r=r+func(s)
    r=int(r,3)

    if r>220 and r%2==0:
        a.add(r)
print(min(a))
