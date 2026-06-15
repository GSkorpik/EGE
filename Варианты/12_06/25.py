def f(n):
    m=1000000000000000
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            if (n//i)%100==13 and n//i!=13:
                m=min(m,n//i)
            if i%100==13 and i!=13:
                m=min(m,n//i)
    if m<1000000000000000:
        return m
    else:
        return 0
k=0
for i in range(2460070,10**9):
    m=f(i)
    if m!=0:
        print(i,m)
        k+=1
    if k==5:
        exit()