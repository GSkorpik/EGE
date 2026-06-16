
m=0
for n in range(1,10000):
    b=bin(n)[2:]
    if n%2==0:
        b1=b+'0'
    else:
        b1=b+'1'
    if b1.count('0')%3==0:
        r='11'+b1[2:]
    else:
        r='10'+b1[2:]
    r=int(r,2)
    if r<400:
        m=max(m,r)

print(m)