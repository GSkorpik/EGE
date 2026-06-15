a=[int(x) for x in open('17.txt')]

k=0
m=1000000
mm=-1000000000
for i in range(len(a)-1):
    a1=a[i]
    a2=a[i+1]
    if (a1**2+a2**2)%10==3:
        m=min(m,a1+a2)
        k+=1
    if (a1+a2)==-186259:
        mm=max(mm,a1,a2)
        print(a1,a2)

print(k,abs(mm))