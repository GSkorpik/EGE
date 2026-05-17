def f(x,a1,a2):
    p=13<=x<=19
    q=17<=x<=23
    a=a1<=x<=a2
    return (not((not(p))<=q))<=(a<=((not(q))<=p))

p=[x+d for x in [13,17,19,23] for d in [-0.1,0,0.1]]
am=0
for a1 in p:
    for a2 in p:
        if all(f(x,a1,a2) for x in p):
            am=max( am,round(a2) -round(a1))

print(am)