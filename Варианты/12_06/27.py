
f=open('27_A.txt')
f.readline()

d=[]
for s in f:
    p=[float(c)for c in s.replace(',','.').split()]
    d.append(p)
print(len(d))
def di(p1,p2):
    x1,y1,x2,y2=*p1,*p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def g(p0):
    c=[ p for p in d if di(p0,p)<1]
    if len(c)>0:
        for p in c: d.remove(p)
        nc=[g(p)for p in c]
        c=c+sum(nc,[])
    return c

cs=[]
while len(d)>0:
    p0=d.pop()
    c=[p0]+g(p0)
    print(len(c))
    cs.append(c)

def centr(kl):
    m=[]
    for p in kl:
        s=sum(di(p,p1) for p1 in kl)
        m.append([s,p])
    return min(m)[1]

cid=[centr(kl) for kl in cs]

print(cid)
k=len(cid)
print(k)

px=sum(x for x,y in cid)
py=sum(y for x,y in cid )

print(int(px/k*10000),int(py/k*10000))