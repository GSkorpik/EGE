K = 3  # количество кластеров

def findClusterNo( x, y ):
  return -1 if y < -10 or y > 30 else \
          0 if x > 18 else \
          1 if y > 20 else \
          2

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-103b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    if clusterNo >= 0:
      clusters[clusterNo].append( (x, y) )

clusters.sort( key=lambda cls: len(cls) )
print( [len(cls) for cls in clusters] )

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

print( "Диаметры:\n", diams )

Q1 = dist( diams[0][0], diams[0][1] )

Q2 = 0
for i in range(K):
  for j in range(K):
    if i != j:
      Q2 = max( [Q2] + [dist(p1,p2) for p1 in diams[i] for p2 in diams[j]] )

print( int(Q1*10_000), int(Q2*10_000) )

