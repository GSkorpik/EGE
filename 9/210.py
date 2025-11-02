k=0
for s in open('9-210.csv'):
    a=sorted(map(int,s.split(',')))
    if a.count(a[-1])==1:
        if len(a)!=len(set(a)):
            b=[x for x in a if a.count(x)>1]
            if a[0]+a[-1]>sum(b):
                k+=1
print(k)