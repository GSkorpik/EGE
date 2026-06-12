print('a m e n | f')
for a in 0,1:
    for m in 0, 1:
        for e in 0, 1:
            for n in 0, 1:
                f=(e and (not(m))) or (m==a) or (not(n))
                if f==0:
                    print(a,m,e,n,'|',f)