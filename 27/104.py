
k=2

def f(x,y):
    return 0 if y>5 else 1

cluster=[[] for i in range(k)]

for s in open('27-104a.txt'):
    x,y =s.replace(',','.').split()
    x,y=float(x),float(y)
    n=f(x,y)
    if n>=0:
        cluster[n].append((x,y))
from math import dist

sc=[]
for i in range(k):
    m=10**10
    for p in cluster[i]:
        s=sum(dist(p,x) for x in cluster[i])

        if s<m:
            m=s
            c=p
    sc.append(c)


print(sc)
print(dist((2.1,5.0),sc[0])*10000,dist((2.1,5),sc[1])*10000)#px
mp=[ (sc[0][i]+sc[1][i])/2 for i in range(2)]
py=dist((2.1,5.0),mp)*10000
print(py)