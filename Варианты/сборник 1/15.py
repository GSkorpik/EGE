
a=list(range(3,61))
b=[x for x in range(2,177) if 177%x==0 ]
for y in range(2,10000):
    c=[x for x in range(2,y) if y%x ==0]
    if c:
        k=1
        for x in range(1,10000):
            k*=(( x in c )<=((x in a) and (x not in b)))
            if k==0:
                break

        if k==1:
            print(y)