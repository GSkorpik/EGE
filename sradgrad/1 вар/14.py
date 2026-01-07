
kmax=0
for x in range(1,8411):
    k = 0
    a=29**293+29**271-x
    while a!=0:
        b=a%29
        a//=29
        if b==0:
            k+=1
    if k>kmax:
        kmax=k
print(kmax)