k=0
maxa=0
a=[int(x) for x in open('17_27629.txt')]
a4=max(x for x in a if 1000<=abs(x)<10000 and abs(x)%100==43)
for i in range(len(a)-1):
    a1=a[i]
    a2=a[i+1]
    if 1000<=abs(a1)<10000 or 1000<=abs(a2)<10000:
        if (a1+a2)**2<a4**2:
            k+=1
            maxa=max(maxa, (a1+a2)**2)

print(k,maxa)