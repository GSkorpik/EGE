for a in range(32767,1000000):
    k=1
    for x in range(100000,1000000):
        k*=((x&32765!=0) or (x&22635!=0))<=(x&a>0)
    if k==1:
        print(a)
        break

#долго работает