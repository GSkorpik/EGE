for n in range(1,256):
    s=bin(n)[2:]

    while len(s) < 8:
        s = '0' + s
    r=s[:2]+s[-2:]
    f=int(r,2)
    if f==10:
        print(n)
