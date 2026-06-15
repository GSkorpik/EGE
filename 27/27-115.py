A = [[],[]]

for s in open('27-115a.txt'):
    x,y,t = s.replace(',','.').split()
    x,y = float(x), float(y)
    if y > 10: A[0].append([x,y,t])
    else: A[1].append([x,y,t])

B = [[],[],[]]
for s in open('27-115b.txt'):
    x,y,t = s.replace(',','.').split()
    x,y = float(x), float(y)
    if x > 20: B[0].append([x,y,t])
    elif y > 22: B[1].append([x,y,t])
    else: B[2].append([x,y,t])

def dist(p1,p2):
    x1,y1,t1 = p1
    x2,y2,t2 = p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

A.sort( key = len )
B.sort( key = len )

c0 = centr(A[0])
c1 = centr(A[1])

D = [ dist(c0,p) for p in A[0]+A[1]
                 if p[2][0]=='Y' and p[2][2:] == 'III']
A1 = int( min(D)*10000 )
A2 = int( max(D)*10000 )
print( A1, A2 )

q, c = [], []
for i in range(3):
  q.append( [p for p in B[i]
               if p[2][0]=='Z' and p[2][2:]=='I'] )
  c.append( centr(B[i]) )
iMin = q.index( min( q, key=len ) )
iMax = q.index( max( q, key=len ) )

B1 = float('inf')
for i in range(3):
  if len(q[i]) > 1:
    r = min( dist(p1, p2) for p1 in q[i] for p2 in q [i] if p1 != p2 )
    B1 = min(B1, r)
B2 = dist(c[iMin], c[iMax])

print( int(B1*10000), int(B2*10000))

