for a in range(1,1000):
    k=1
    for x in range(1,1000):
        for y in range(1,1000):
            k*=(x+y<=30)or (y<=x+2) or (y>=a)
    if k==1:
        print(a)

