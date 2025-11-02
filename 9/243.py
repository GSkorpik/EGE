
k=0

for s in open('9-243.csv'):
    a=sorted(map(int,s.split(',')))

    if len(set(a))==2:
        a1=a.count(a[0])
        a2 = a.count(a[-1])
        if a1+a2>=4:
            if a[0]+a[-1]<a[0]*(a1-1)+a[-1]*(a2-1):
                suma=sum(a)


print(suma)