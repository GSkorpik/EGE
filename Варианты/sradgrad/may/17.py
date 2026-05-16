k=0
m=0
a=[int(x) for x in open('17.txt')]
am=max(x for x in a if 10<=x<100 and x%10==3)
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    a4=abs(max(a1,a2,a3))+abs(min(a1,a2,a3))
    if a1<0 and a2<0 and a3<0 and ( ((100<=abs(a1)<1000)+(100<=abs(a2)<1000)+(100<=abs(a3)<1000))==0) and (a4<=am**2):
        k+=1
        m=max(m,a4)
print(k,m)
