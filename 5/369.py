def f(n):
    a='0123456789abc'
    if n<13:
        return a[n]
    else:
        return f(n//13)+a[n%13]




rm=0
a=[]
for n in range(1,100):
    b=f(n)
    su = 0
    for s in b:
        su+=int(s,13)
    b=b+f(su%13)

    su1 =0
    for s in b:
        su1+=int(s,13)
    b = b + f(su1 % 13)
    r=int(b,13)
    #print((f(n)),b,n,r)
    if r<6000 :
        a.append((r,n))
print(sorted(a,reverse=True)[0])

