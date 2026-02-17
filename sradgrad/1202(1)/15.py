# не так
for a in range(89200,100000):
    f=1
    for x in range(89200,100000):
        for y in range(89200,100000):
            f*=(((y<a)and(x<a)) or (89241<5*y+x))
    if f==1:
        print(a,f)
