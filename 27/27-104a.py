from math import dist

K = 2  # количество кластеров

def findClusterNo( x, y ):
  return 0 if x < 2 else 1

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-104a.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    clusters[clusterNo].append( (x, y) )

print( "Кластеры:" )
for cluster in clusters:
  print( len(cluster) )

from math import dist

def getCenter( cluster ):
  minSumDist = float('inf')
  for pCenter in cluster:
    sumDist = sum( dist(pCenter,p) for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
  return center

centers = [ getCenter(cluster) for cluster in clusters ]

print( "Центры:\n", centers )

midPoint = [ (centers[0][i]+centers[1][i])/2 for i in range(2) ]
print( "Середина отрезка между центрами:\n", midPoint )

pt = (2.1, 5.0)
distToPoint = [ dist( pt, c ) for c in centers ]
print( "Расстояния:\n", distToPoint )

Px = min( distToPoint )
Py = dist( pt, midPoint)

print( int(Px*10_000), int(Py*10_000) )


