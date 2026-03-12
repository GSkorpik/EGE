
for n in range(1,200):
    b=bin(n)[2:]
    if n%3==0:
        r=b+b[-3:]
    else:
        r=b+bin((n%3)*3)[2:]

    r=int(r,2)
    if 120<r<140:
        print(n,r)