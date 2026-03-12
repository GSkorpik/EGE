k=0
kmax=[]

a=[int(x) for x in open('17.txt')]
maxo=max(x for x in a if x<0 and 100<=abs(x)<=999 and abs(x)%6==0)

for i in range(len(a)-1):
    a1 = a[i]
    a2 = a[i + 1]
    if (a1<0)+(a2<0)==1:
        if (a1+a2)>maxo:
            k+=1
            kmax.append((a1**2)+(a2**2))
print(k,max(kmax))
