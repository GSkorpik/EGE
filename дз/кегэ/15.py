p=[]
for x in range(1,20000):
    y=78125-4*x
    if y>0:
        p.append([x,y])
print(p[0],p[-1])
for a in range(0,100000):
    if all((((y+x*4)!=78125) or ((a>x) and (a>y))) for x,y in p):
        print(a)
        break