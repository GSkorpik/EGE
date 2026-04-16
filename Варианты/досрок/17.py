k=0
m=0
a=[int(x) for x in open('17.txt')]
a23=min(int(x) for x in a if x%23==0)

for i in range(len(a)-1):
    if a[i]%a23==0 or a[i+1]%a23==0:
        k+=1
        m=max(m,a[i]+a[i+1])

print(k,m)