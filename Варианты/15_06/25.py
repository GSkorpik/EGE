def p(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return 0
    return 1



k=0
for n in range(2000000,10**10):
    for x in range(601,1000):
        if p(x)==1:

            for y in range(601, 1000):
                if p(y) == 1:

                    for z in range(1, 1000):
                        if p(z) == 1:

                            for w in range(1, 1000):
                                if p(w) == 1:

                                    if p(x)+p(y)+p(z)+p(w)==4:
                                        if x*y*z*w==n:
                                            k+=1
                                            print(n,max(x,y,z,w))
                                    if k==5:
                                        exit()
                                    print(n,x,y,z,w)
                                    if x*y*z*w>n:

                                        break
