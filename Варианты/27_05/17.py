

f=[int(x) for x in open('17_29128.txt')]
s=sum(f)

k=0
m=10000000000
for i in range(len(f)-2):
    f1=f[i]
    f2=f[i+1]
    f3=f[i+2]
    if (100<=abs(f1)<1000) and  (100<=abs(f2)<1000) and (100<=abs(f3)<1000) and f1*f2*f3>s:
        k+=1
        m=min(m,abs(f1*f2*f3))

print(k,m)