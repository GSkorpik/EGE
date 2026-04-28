
a=[int(x) for x in open('17-1.txt')]
s=sum(a)/len(a)
k=0
m=0
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    if (a1<s)+(a2<s)+(a3<s)>=2:
        if str(a1).count('6')+str(a2).count('6')+str(a3).count('6')>0:
            k+=1
            m=max(m,a1+a2+a3)



print(k,m)

