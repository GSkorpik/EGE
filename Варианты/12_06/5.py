

for n in range(1,1000):
    b=bin(n)[2:]
    if n%7==0:
        r=b[:3]+b
    else:
        r=b+bin((n%7)*7)[2:]
    r=int(r,2)
    if r<419 and n%2!=0:
        print(n)