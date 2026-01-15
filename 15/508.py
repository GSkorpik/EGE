for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=((a%25==0)and (((x%24==0 ) and (x%75==0)) <= (x%a==0)))
    if k==1:
        print(a)

