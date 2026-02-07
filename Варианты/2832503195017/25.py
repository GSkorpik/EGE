def d(n):
    a=set()
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
           a.add(i)
           a.add(n//i)
    if len(a)<6:
        return 0
    else:
        return sorted(a)[-6]


k=0
for n in range(300000001,10000000000000):
    dd=d(n)
    if dd>0:
        print(n,dd)
        k+=1
    if k==5:
        break