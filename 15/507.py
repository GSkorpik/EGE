for a in range(0,1000):
    k=1
    for x in range(1,1000):
        k*=((x%2==0)<=(x%3!=0))or (x+a>=80)
    if k==1:
        print(a)
        break