for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=(((x&13!=0) or (x&a==0))<=(x&13!=0)) or (x&a!=0) or (x&39==0)
    if k==1:
        print(a)
        break