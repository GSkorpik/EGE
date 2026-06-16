def f(n):
    k=0
    while n!=0:
        a=n%7
        if a%2==0:
            k+=1
        n//=7
    return k
m=10**10
for x in range(0,1000):
    a=7**720+7**170+7**70-x
    k=f(a)
    m=min(m,k)
    if k==715:
        print(x)