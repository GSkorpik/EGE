a=[[],[]]
from math import dist
def c(cl):
    m=[]
    for p in cl:
        s=sum(dist(p[0:2],p1[0:2]) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

for s in open('27-115a.txt'):
    x,y,t=s.replace(',','.').split()
    x,y=float(x), float(y)
    if y>10: a[0].append([x,y,t])
    else: a[1].append([x,y,t])

a.sort(key= len)

c0=c(a[0])
c1=c(a[1])
d=[dist(c0[:2],p[:2]) for p in a[0]+a[1] if p[2][0]=='Y' and p[2][2:]=='III']

a1=int(min(d)*10000)
a2=int(max(d)*10000)
print(a1,a2)
b=[[],[],[]]

for s in open('27-115b.txt'):
    x,y,t = s.replace(',','.').split()
    x,y = float(x), float(y)
    if x > 20: b[0].append([x,y,t])
    elif y > 22: b[1].append([x,y,t])
    else: b[2].append([x,y,t])

b.sort( key = len )

q,cc=[],[]
for i in range(3):
    q.append([p for p in b[i] if p[2][0]=='Z' and p[2][2:]=='I'])
    cc.append(c(b[i]))

imi=q.index(min(q,key=len))
ima=q.index(max(q,key=len))

b1=10**10
for i in range(3):
    if len(q[i])>1:
        r=min(dist(p1[:2],p2[:2]) for p1 in q[i] for p2 in q[i] if p1[:2]!=p2[:2])
        b1=min(b1,r)
b2=dist(cc[imi][:2],cc[ima][:2])
print(int(b1*10000),int(b2*10000))