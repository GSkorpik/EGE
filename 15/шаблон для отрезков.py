def f(x,a1,a2):
    #концы отрезков меняются
    p=10<=x<=40
    q=5<=x<=15
    r=35<=x<=50
    a=a1<=x<=a2
    return (p<=q) or ((not a)<=r)# меняется

                #концы отрезков меняются
p=[x+d for x in [5,10,15,35,40,50] for d in [-0.1,0,0.1]]
am=10**10# минимум
for a1 in p:
    for a2 in p:
        if all(f(x,a1,a2) for x in p):
            am=min(am,round(a2)-round(a1))# минимум

print(am)