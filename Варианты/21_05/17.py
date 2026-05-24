
f=[int(x) for x in open('17_29971.txt')]
fm=max( x for x in f if abs(x)%100==33)
k=0
m=0
for i in range(len(f)-2):
    f1=f[i]
    f2=f[i+1]
    f3=f[i+2]
    s=f1+f2+f3
    if (10<=abs(f1)<100 )+(10<=abs(f2)<100 )+(10<=abs(f3)<100 ) ==2 and s**2<fm:
        k+=1
        m=max(m,s)

print(k,m)