for a in range(1,100000):
    k=1
    for x in range(1,100000):
        k*=((x&32765!=0) or (x&22635!=0))<=(x&a>0)
        if k==0:
            break
    if k==1:
        print(a)
        break

#долго работает 32767