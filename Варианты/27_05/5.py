m=0
for n in range(1,100000):
    b=bin(n)[2:]
    if n%2==0:
        b=b+'0'
    else:
        b=b+'1'
    if b.count('1')%3==0:
        r='11'+b[2:]+'0'
    else:
        r='10'+b[2:]+'1'

    r=int(r,2)
    if r<=4200:
        m=max(m,r)
print(m)