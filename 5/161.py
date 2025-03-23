for n in range(1,101):

    s=bin(n)[2:]
    r=s[::-1]
    f=int(r,2)
    if f==7:
        print(n)