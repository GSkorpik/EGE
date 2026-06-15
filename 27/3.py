f=open('27-3a.txt')
f.readline()

data=[]
for s in f:
    p= [float(c) for c in s.replace(',','.').split()]
    data.append(p)
print(len(data))
#print(data[:20])
def dist(p1,p2):      
	x1,y1,x2,y2 = *p1, *p2
	return ((x1-x2)**2+(y1-y2)**2)**0.5

def getCluster(p0):
	cluster=[p for p in data if dist(p0,p)<0.5]
	if len(cluster)>0:
		for p in cluster: data.remove(p)
		next_cluster=[getCluster(p) for p in cluster]
		cluster=cluster + sum(next_cluster, [])
	return cluster
 
clusters=[]
while len (data)>0:
	p0=data.pop()
	cluster = [p0] + getCluster(p0)
	print(len(cluster))
	clusters.append(cluster)

def center(kl): 
	m=[]
	for p in kl:
		s=sum(dist(p,p1) for p1 in kl)
		m.append ([s,p])
	return min (m)[1]

centroid=[center(kl) for kl in clusters]

print (centroid)

K=len(centroid)
print(K)

px=sum (x for x,y in centroid)
py=sum (y for x,y in centroid)

print( int(px/K*10000), int(py/K*10000) )

