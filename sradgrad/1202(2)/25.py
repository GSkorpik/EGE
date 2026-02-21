def d(n):
    a=set()
    for i in range(1,round(n**0.5)-1):
        if n%i==0:
            a.add(i)
            a.add(n//i)
    return len(a)


for x in range(10**9-1,10**8+1,-1):
    k=d(x)
    if (x-k)%17==0 and x-k>0:
        print(x)