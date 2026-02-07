
for n in range(1,1000):
    b=bin(n)[2:]
    if n%2==0:
        b='1'+b
    else:
        b=b+'0'
    if b.count('1')%2==0:
        r=b+'1'
    else:
        r=b+'0'
    r=int(r,2)
    if r>228:
        print(n)
        break