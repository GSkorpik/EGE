for a in range(1,1000):
    k=1
    for x in range(1,100):
        for y in range(1,100):
            k*=((x<a)or (y<a) or (x+2*y>50))
    if k==1:
        print(a)
        break