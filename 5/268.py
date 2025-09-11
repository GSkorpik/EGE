a=set()

for n in range(1,1000):
    b=bin(n)[2:]
    a1=b.count('1')
    a0=b.count('0')
    if a1>a0:
        r=b+'1'
    else:
        r=b+'0'

    a1 = b.count('1')
    a0 = b.count('0')
    if a1 > a0:
        r = b + '1'
    else:
        r = b + '0'

    r=int(r,2)
    if r<57:
        a.add(r)
print(max(a))