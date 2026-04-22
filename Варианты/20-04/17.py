
a=[int(x) for x in open('17-338.txt')]
am=min(a)
k=0
m=0
for i in range(len(a)-1):
    a1=a[i]
    a2=a[i+1]
    if a1%117==am or a2%117==am:
        k+=1
        m=max(m,a1+a2)

print(k,m)

