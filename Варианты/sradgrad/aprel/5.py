

maxn=0
for n in range(1,10000):
    p=1
    ma=0
    mi=1000000
    for ii in str(n):
        p=p*int(ii)
        ma=max(ma,int(ii))
        mi=min(mi,int(ii))
    m=ma+mi
    t1=p+m
    t2=p*m
    r=str(t1)+str(t2)

    if int(r)==23126:

        maxn=max(maxn,n)

print(maxn)