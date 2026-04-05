
f=0
ff=0
for x in range(2000000,1000000000000):
    for a in range(1,25):
        if ff==1:
            ff=0
            break
        for b in range(1,25):
            if x==2**a+2**b:
                print(x,a+b)
                f+=1
                ff=1
                break
    if f==5: break