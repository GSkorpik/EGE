def f(n):
    alf='0123456789ab'
    s=''
    while n!=0:
        s=alf[n%12]+s
        n//=12
    return s
r1=0
for n in range(143,1000):
    s=f(n)
    if n%12==0:
        r=s+s[-3:]
    else:
        b=n%12*3
        r=f(b)+s
    r=int(r,12)
    if r < 58000 and r > r1:
        r1 = r
        n1 = n
print(n1, r1)
