for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=((x&56!=0)<=((x&48==0)<=(x&a!=0)))
    if k==1:
        print(a)
        break