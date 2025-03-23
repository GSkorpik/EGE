def f(n):
    s=''
    while n != 0:
        a = n % 3
        s = str(a) + s
        n//=3
    return s
for n in range(1,100):
    s=f(n)
    if n%2==0:
        r='1'+s+'00'
    else:
        summ=sum(map(int,s))
        r=s+f(summ)
    r=int(r,3)
    if r>168:
        print(n,r)
        break