
for p in range(100,4,-1):
    for q in range(100,4,-1):
        r=min(p,q,10)
        for a in range(1,r):
            for b in range(1,r):
                for c in range(r):
                    for d in range(r):
                        if len({a,b,c,d})==4:
                            a1=a*p**3+b*p**2+c*p+1
                            b1=b*q**3+c*q**2+1*q+d
                            if a1==b1:
                                print(a1,p,q)
                                exit()