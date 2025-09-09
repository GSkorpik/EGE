y=1234

maxs=0
for n in range(2,11):
    s=0
    a=y
    while a!=0:
        x=a%n
        a//=n
        s+=x

    maxs=max(s,maxs)
    if maxs==s:
        maxn=n


    if s > maxs:
        maxs=s
        maxn=n

print(s,maxs,maxn)









