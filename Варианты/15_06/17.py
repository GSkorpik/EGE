
a=[int(x) for x in open('17_27470.txt')]
am=min(x for x in a if x>0)
m=10**10
k=0
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]

    if abs(a1)%am==0 or abs(a2)%am==0 or abs(a3)%am==0:
        p=(a1*a2*a3)
        if abs(p)%10==4:
            m=min(m,p)
            k+=1
print(k,m)