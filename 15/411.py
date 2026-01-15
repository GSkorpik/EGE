for a in range(1,10000):
    k=1
    for x in range(1,10000):
        k*=((a%9==0)and (280%x==0)<=((a%x!=0)<=(730%x!=0)))
    if k==1:
        print(a)
        break