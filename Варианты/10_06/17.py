

a=[int(x) for x in open('17.txt')]
am=max(x for x in a if abs(x)%100==36)
k=0
m=0
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    if ((1000<=abs(a1)<10000) +(1000<=abs(a2)<10000) +(1000<=abs(a3)<10000))<=2:
        if a1+a2+a3<=am:
            k+=1
            m=max(m,a1+a2+a3)

print(k,m)