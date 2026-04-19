m=0
for n in range(1,1000):
    b=bin(n)[2:]
    if n%3==0:
        r=b+str(b)[-3:]
    else:
        r=b+str(bin((n%3)*3)[2:])

    r=int(r,2)
    if r<130:
        m=max(m,n)

print(m)