def func(n):
    s=''
    while n!=0:
        a=n%3
        s = str(a) + s
        n//=3
    return s

a=set()
for n in range(1,1000):
    s=func(n)
    if n%2==0:
        s='2'+s
        tr=func(int(s[-1])*2)
        s=s+tr

    else:
        tr = func(int(s[0]) * 2)
        s = tr + s
        s = s + '2'
    r=int(s,3)
    if r>100:
        a.add(r)
print(min(a))

