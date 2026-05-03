def f(n):
    s=''
    while n!=0:
        a=n%3
        s=str(a)+s
        n//=3

    if s[::-1]==s:
        return True
    return False

k=0
m=1000000000000000000000
a=[int(x) for x in open('17-370.txt')]
am=max(x for x in a if 100<=abs(x)<1000 and f(abs(x))==True)

for i in range(len(a)-1):
    a1=a[i]
    a2=a[i+1]
    if ((1000<=abs(a1)<10000) + (1000<=abs(a2)<10000))==1:
        if (a1**2+a2**2)%am==0:
            k+=1
            m=min(m,(a1**2+a2**2))
print(k,m)

