
for a in range(1,1000):
    k=1
    for x in range(1,1000):
        f=(x&71==0) or ((x&13==0)<= (not(x&a==0)))
        k*=f
    if k==1:
        print(a)