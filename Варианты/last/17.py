a=[ int(x) for x in open('17-1.txt')]
am=min( x for x in a if x>0 and x%9==0)
k=0
m=0
for i in range(len(a)-1):
    a1=a[i]
    a2=a[i+1]
    if a1!=a2 and abs(a1-a2)%am==0:
        k+=1
        m=max(m,a1+a2)

print(k,m)