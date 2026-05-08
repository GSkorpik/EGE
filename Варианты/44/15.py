

for a in range(1,1000):
    k=1
    for x in range(0,100):
        for y in range(0,100):
            k*=((7*y+x<a)or (2*x+3*y>98))
    if k==1:
        print(a)
        break