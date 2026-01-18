for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=((x%3==0)<=(x%5!=0))or (x+a>=70)
    if k==1:
        print(a)
        break