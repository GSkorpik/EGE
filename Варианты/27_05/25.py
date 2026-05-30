def f(n):
    k=0
    m=0
    for i in range(1,round(n**0.5)+1):
        if n%i==0:
            if ((n//i)-i)%67==0 and ((n//i)-i)>0:
                k+=1
                m=max(m,n//i,i)

    if k>=6:
        return m
    return False
for n in range(500000,700000+1):
    s=f(n)
    if s!=False:
        print(n,s)
