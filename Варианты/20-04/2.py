print('a b c d | f')
for a in 0,1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:

                f=(a<=d) and  not(b<=c)

                if f==1:
                    print(a,b,c,d,'|',f)


