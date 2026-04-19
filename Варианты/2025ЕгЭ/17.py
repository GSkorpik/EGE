
a=[int(x) for x in open('17_23201.txt')]
a7=min(x for x in a if 100<=x<1000 and x%10==7)
k=0
m=10000000000
for i in range(len(a)-1):
    if (100<=a[i]<1000 or 100<=a[i+1]<1000) and (a[i]+a[i+1])%a7==0:
        k+=1
        m=min(m,a[i]+a[i+1])

print(k,m)