
K = 2  # количество кластеров

def findClusterNo( x, y ):
  return 0 if y > 10 else \
         1

#------------------------------------------------

clusters = [ [] for i in range(K) ]

#for s in open("27-102a.txt"):
for s in open("27-103a.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    if clusterNo >= 0:
      clusters[clusterNo].append( (x, y) )

from math import dist

diams = [0]*K
for k in range(K):
  maxDist = float('-inf')
  for p1 in clusters[k]:
    for p2 in clusters[k]:
      d = dist(p1,p2)
      if d > maxDist:
        maxDist = d
        diams[k] = (p1, p2)

print( "Р”РёР°РјРµС‚СЂС‹:\n", diams )

Px = min( p1[0]+p2[0] for p1, p2 in diams )
Py = max( p1[1]+p2[1] for p1, p2 in diams )

print( int(abs(Px)*10_000), int(abs(Py)*10_000) )

