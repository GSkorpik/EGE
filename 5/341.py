def f(n):
    a='0123456789ab'
    if n<12:
        return a[n]
    else:
        return f(n//12)+a[n%12]
a=[]
for n in range(12,1000):
    s=f(n)
    if n%12==0:
        d=s+s[-2:]
    else:
        d=s+f((n%12)*9)
    r=int(d,12)
    if r>300:
        a.append(r)
print(min(a))
