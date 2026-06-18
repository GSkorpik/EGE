from math import dist

def ce(cl):
    m=[]
    for p in cl:
        s=sum( dist(p[:2],p1[:2]) for p1 in  cl)
        m.append([s,p])
    return min(m)[1]

a=[[],[]]

for s in open('27-1-A.txt'):
    x,y,t=s.replace(',','.').split()
    x,y=float(x),float(y)
    if y>10: a[0].append([x,y,t])
    else: a[1].append([x,y,t])

a.sort(key=len)

c0=ce(a[0])
c1=ce(a[1])
#print(c0,c1)

d=[dist(c0[:2],p[:2]) for p in a[0]+a[1] if p[2][0]=='Y' and p[2][-3:]=='III']

a1=min(d)*10000
a2=max(d)*10000

print(a1,a2)
