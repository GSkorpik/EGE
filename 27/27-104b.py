from math import dist

K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if x > 3 else \
         1 if y < -2 else \
         2

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-104b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    clusters[clusterNo].append( (x, y) )

clusters.sort( key=lambda cls: len(cls) )

print( "Кластеры:" )
for cluster in clusters:
  print( len(cluster) )

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

Q1 = 0
for i in range(3):
  Q1 += sum( 1 for p in clusters[i] if dist(p, centers[-1]) <= 5)
  print( Q1 )

Q2 = 0
for i in range(3):
  Q2 += sum( 1 for p in clusters[i] if dist(p, centers[0]) > 5)
  print( Q2 )

print( Q1, Q2 )
