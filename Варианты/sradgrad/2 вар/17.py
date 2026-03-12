mini=10000000000
k=0
a=[int(x) for x in open('17.txt')]
mmax=max((int(x) for x in a if 1000<=abs(x)<10000 and x<0 and abs(x)%9==0))
for i in range(len(a)-1):
    a1=a[i]
    a2=a[i+1]
    if a1*a2<0:
        if a1+a2>mmax:
            k+=1
            mini=min(mini,a1**2+a2**2)

print(k,mini)