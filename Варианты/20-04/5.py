
for n in range(100,10000):
    b=bin(n)[2:]
    o=b.count('0')
    i=b.count('1')
    if o==i:
        b1=b+b[-1]
    else:
        if o>i:
            b1=b+'1'
        else:
            b1 = b + '0'
    o = b1.count('0')
    i = b1.count('1')
    if o == i:
        b2 = b1 + b1[-1]
    else:
        if o > i:
            b2 = b1 + '1'
        else:
            b2 = b1 + '0'

    r=int(b2,2)
    if r%4==0 and r%8!=0:
        print(n,r)
        break