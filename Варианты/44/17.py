def f(n):
    k=0
    while n!=0:
        k+=1
        n//=6
    return k


a=[int(x) for x in open('17-290.txt')]

m=0
k=0
for i in range(0,len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    if ((a1%5==1 )+(a2%5==1) + (a3%5==1 ))>=1:
        if f(a1)==4 and f(a2)==4 and f(a3)==4 :
            k+=1
            m1=max(a1,a2,a3)
            m2=min(a1,a2,a3)
            m=max(m,m1-m2)

print(k,m)