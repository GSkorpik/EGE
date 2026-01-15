for a in range(101,1000):
    k=1
    for x in range(1,10000):
        k*=(((x%a==0) and (x%36==0)) <= (x%324==0))
    if k==1:
        print(a)
        break