
K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if x > 20 else \
         1 if y > 22 else \
         2

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-101b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    if clusterNo >= 0:
      clusters[clusterNo].append( (x, y) )

clusters.sort( key=lambda x: len(x) )
print( [len(cls) for cls in clusters] )

from math import dist

centers = []
for k in range(K):
  minSumDist = float('inf')
  for pCenter in clusters[k]:
    sumDist = sum( dist(pCenter,p)
                   for p in clusters[k] )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
  centers.append( center )

print( "Центры:\n", centers )
maxq1=0
maxq2=0
for i in range(3):
    Q1 = sum( 1 for p in clusters[i]
                if dist(p,centers[i]) <= 1.2  )
    Q2 = sum( 1 for p in clusters[i]
                if dist(p,centers[i]) <= 0.75  )
    maxq1=max(maxq1,Q1)
    maxq2 = max(maxq2, Q2)
print( maxq1, maxq2 )

