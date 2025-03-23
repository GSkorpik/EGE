for n in range(1,100):
    r=oct(n)[2:]
    if n%5==0:
        r=r+r[:3]

    else:
        a=n%5
        r=r+bin(a)[2:]
    s = int(r, 8)
    if s>=35000:
        print(n,r,s)
