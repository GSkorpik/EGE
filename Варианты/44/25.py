
for N in range(100000000,300000000):
    for m in range(0,30,2):
        n1=1
        for n in range(1,31,2):

            if N==2**m*7**n:
                print(N,m+n)
                n1=n
        if 2**m*7**n1>N:
            break
