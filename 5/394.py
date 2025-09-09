def f(n):
    alf='0123456789abcdefghij'
    s=''
    while n!=0:
        s=alf[n%20]+s
        n//=20
    return s
a=set()
for n in range(1,1000):
    s=f(n)

    a1='1'*len(s)
    r=n+int(a1,20)
    r=f(r)
    if n%2==1:
        r='1'+str(r)
    else:
        r=r

    p=r.count('a')
    p+= r.count('b')
    p+= r.count('c')
    p += r.count('d')
    p += r.count('e')
    p += r.count('f')
    p += r.count('g')
    p += r.count('h')
    p += r.count('i')
    p += r.count('j')
    if len(r)>=3 and p>=2:
        a.add(n)

print(min(a))