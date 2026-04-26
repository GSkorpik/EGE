
for n in range(103,1000):
    b=bin(n)[2:]
    print(b)
    o=b.count('0')
    i=b.count('1')
    if o==i:
        b1=b+b[-1]
        print(b)
    else:
        if i<o:
            b1=b+'1'
            print(b1)
        else:
            b1 = b + '0'
            print(b1)
    o = b1.count('0')
    i = b1.count('1')
    if o == i:
        b2 = b1 + b1[-1]
        print(b2)
    else:
        if i<o:
            b2 = b1 + '1'
            print(b2)
        else:
            b2 = b1 + '0'
            print(b2)
    o = b2.count('0')
    i = b2.count('1')
    if o == i:
        b3 = b2 + b2[-1]
        print(b3)
    else:
        if i < o:
            b3 = b2 + '1'
            print(b3)
        else:
            b3 = b2 + '0'
            print(b3)
    r=int(b3,2)
    if r%4==0 and r%8!=0:
        print(n,r)
        break