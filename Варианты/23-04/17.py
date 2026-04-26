
a=[int(x) for x in open('17-340.txt')]
b=[ int(x) for x in a if x%22==0]
sr=sum(b)//len(b)
k=0
maxx=0
for i in range(len(a)-1):
    a1=a[i]
    a2=a[i+1]
    b1=oct(a1)[2:]
    b2=oct(a2)[2:]
    max1=max(int(x) for x in str(b1))
    i1=b1.index(str(max1))
    min1=min(int(x) for x in str(b1))
    i2 = b1.index(str(min1))
    max2 = max(int(x) for x in str(b2))
    i3 = b2.index(str(max2))
    min2 = min(int(x) for x in str(b2))
    i4 = b2.index(str(min2))
    if i2>i1 and i4>i3:
        if a1+a2<sr:
            k+=1
            maxx=max(maxx,a1+a2)

print(k,maxx)


