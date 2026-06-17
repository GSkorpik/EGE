
k = 2  # количество кластеров

def f(x,y):# Разгроничение между кластерами
    return 0 if y>10 else 1

cluster=[[] for i in range(k)]

for s in open('27-101a.txt'):
    x,y =s.replace(',','.').split()
    x,y=float(x),float(y)
    N=f(x,y)
    if N >=0:
        cluster[N].append((x,y))

from math import dist


cs=[]
for i in range(k):
    m=10**10
    for p in cluster[i]:
        s=sum(dist(p, x) for x in cluster[i])

        if s<m:
            m=s
            c=p
    cs.append(c)

print('центры:\n',cs)
px=min(dist(c,(1,1)) for c in cs)
py=max(dist(c,(1,1)) for c in cs)
print(int(abs(px)*10000),int(abs(py)*10000))#Зависит от задания


