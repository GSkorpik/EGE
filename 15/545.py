for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=((x%10==0) and (x%26==0)and(x>=300))<=(a<=x)
    if k==1:
        print(a)
