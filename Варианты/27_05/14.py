f=0
for y in range(0,30):
    for x in range(0,30):
        a='7F0105'
        b='K70AB'
        a1=int(a,30)
        b1=int(b,30)
        a2=a1+y*30**3+x*30
        b2=b1+y*30**2
        if (a2+b2)%19==0:
            f+=1
    if f>1:
        print(y)
        break