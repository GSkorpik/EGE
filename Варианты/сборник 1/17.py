f=[int(x) for x in open('17var01.txt')]
ma=max(x for x in f if 10<=abs(x)<100)
mi=min(x for x in f if 10<=abs(x)<100)

k=0
m=0
for i in range(len(f)-2):
    f1=f[i]
    f2=f[i+1]
    f3=f[i+2]
    if (10<=abs(f1)<100 )+(10<=abs(f2)<100 )+(10<=abs(f3)<100 )>=2:
        if f1+f2+f3>ma+mi:
            k+=1
            m=max(m,f1+f2+f3)

print(k,m)