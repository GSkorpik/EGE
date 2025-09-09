
for n in range(0,10000000):
    b=bin(n)[2:]
    c1 = b.count('1')
    c0 = b.count('0')
    a = bin(c1)[2:]
    c = bin(c0)[2:]
    r=a+c
    r=int(r,2)
    if r==156:
        print(n)
        break
