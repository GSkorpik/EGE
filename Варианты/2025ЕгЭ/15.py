
for a in range(0,1000):
    k=1
    for x in range(0,1000):
        for y in range(0,1000):
            k*=(x*y>a)or (x>y)or(11>x)

    if k==1:
        print(a)

