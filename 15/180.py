for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=(x&a!=0)<=(((x&17==0)and(x&5==0))<=(x&3!=0))
    if k==1:
        print(a)
