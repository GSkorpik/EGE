def f(n):
    a='0123456789abc'
    if n<13:
        return a[n]
    else:
        return f(n//13)+a[n%13]


su=0
su1=0
rm=0
a=[]
for n in range(1,1000):
    b=f(n)
    for s in b:
        su+=int(s,13)
    b=b+str(su%13)
    for s in b:
        su1+=int(s,13)
    b = b + str(su1 % 13)
    r=int(b,13)

    if r<6000 :
        if r>=rm:
            rm=r
            nm=n
            print(nm,rm)
