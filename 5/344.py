
for n in range(11,100):
    s=''
    i=''
    k1=0
    k2=0
    while n != 0:
        a = n % 3
        s = str(a) + s
        n //= 3
    k2 =s.count('2')+ s.count('0')
    k1=s.count('1')


    if k2>k1:
        i='22'+s
    else:
        i='11'+s
    r=int(i,3)
    print(r)

