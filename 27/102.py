

k=3

def f(x,y):
    return -1 if y<0 or x<0 or x>30 else \
            0 if y<20 else \
            1 if x>19 else 2

cluster=[[] for i in  range(k)]
for s in open('27-102b.txt'):
    x,y=s.replace(',','.').split()
    x,y=float(x), float(y)
    n=f(x,y)
    if n>=0:
        cluster[n].append((x,y))

from math import dist
cs=[]
ac=[]
for i in range(k):
    m=10**10
    mm=0
    for p in cluster[i]:
        s=sum(dist(p, x) for x in cluster[i])
        ss=sum(dist(p,x) for x in cluster[i])
        if s<m:
            m=s
            c=p
        if ss>mm:
            mm=ss
            cc=p

    ac.append(cc)

    cs.append(c)


print('центры:\n',cs)
print(ac)
print('a')
print((ac[0][0]+ac[0][1])*10000)
print((ac[1][0]+ac[1][1])*10000)
print('b')
print(ac[1][0]*10000)
print(ac[0][1]*10000)