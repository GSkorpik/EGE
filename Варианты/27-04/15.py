for a in range(1,3000):
    k=1
    for x in range(1,10000):
        k*=(((x%a!=0)or (x%36==0) and (x%126==0)) and (a>1000))
    if k==1:
        print(a)
        break