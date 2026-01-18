for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=(x%a==0)or ((70<=x<=80)<=(x%18!=0))
    if k==1:
        print(a)
