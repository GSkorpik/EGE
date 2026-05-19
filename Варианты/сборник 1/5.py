for n in range(1,1000):
    b=bin(n)[2:]
    if n%3==0:
        b1=b+b[-3:]
    else:
        t=((n%3)+1)*3
        b1=b+bin(t)[2:]
    r=int(b1,2)
    if r<=416:
        print(r)