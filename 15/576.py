def f(x,a1,a2):
    p=128764<=x<=775637
    q=280932<=x<=894567
    r=754683<=x<=929871
    a=a1<=x<=a2
    return ((not a)<=((p==q)<=(r==q)) )

p=[x+d for x in [128764,280932,754683,775637,894567,929871] for d in [-0.1,0,0.1]]
am=10**100
for a1 in p:
    for a2 in p:
        if all(f(x,a1,a2) for x in p):
            am=min(am,round(a2)-round(a1))
print(am)
