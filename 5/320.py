a=[]
def f(n):
    s=''
    while n!=0:
        a=n%3
        s=str(a)+s
        n//=3
    return s

rm=111111

for n in range(10,1000):
    t=f(n)
    if n%2==0:
        t+=t[-2:]
    else:
        s=sum(map(int,t))
        s3=f(s)
        t+=s3
    r=int(t,3)
    if r<rm:
        rm=r
        nm=n
print(nm)