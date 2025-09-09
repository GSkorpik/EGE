def f(n):
    s=''
    while n!=0:
        a=n%3
        s=str(a)+s
        n//=3
    return s
a=[]
for n in range(1,10000):
    s=f(n)
    summ=sum(map(int,s))
    if summ%3==0:

        r=s.replace('1','!')
        r=r.replace('0','1')
        r = r.replace('!', '0')
        r='10'+r
    else:
        r=s+'101'
        r='22'+r[2:]

    r=int(r,3)

    if r>314:
        a.append((r,n))

print(sorted(a,reverse=False)[0])