for a in range(1,1000):
    k=1
    for x in range(1,1000):
        for y in range(1,1000):
            k*=(x%33==0)<=((x%a!=0)<=(x%242!=0))
    if k==1:
        print(a)

