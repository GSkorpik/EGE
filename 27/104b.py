k=3
def f(x,y):
    return 0 if x>3 else \
            1 if y<-2 else 2

c=[[] for i in range(k)]

for s in open('27-104b.txt'):
    x,y =s.replace(',','.').split()
    x,y=float(x),float(y)
    n=f(x,y)
    if n>=0:
        c[n].append((x,y))

#print(len(c))
from math import dist
c.sort(key= len)

def getCenter( cluster ):
  minSumDist = float('inf')
  for pCenter in cluster:
    sumDist = sum( dist(pCenter,p) for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
  return center

cs = [ getCenter(cluster) for cluster in c ]
q1=0
q2=0
for i in range(k):
    q1+= sum(1 for p in c[i] if (dist(cs[2],p)<=5))
    q2+= sum(1 for p in c[i] if (dist(p,cs[0])>5))
    print(q2)

print(q1,q2)
