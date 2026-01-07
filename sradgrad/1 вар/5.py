for n in range(1,10000):
    b=bin(n)[2:]
    if n %5==0:
        r=b+'11'
    else:
        c=n//5
        c=bin(c)[2:]
        r=b+c
    r=int(r,2)
    if r%2!=0 and r>=783:
        print(n)
        break