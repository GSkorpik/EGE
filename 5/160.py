for i in range(0,256):

    b=bin(i)[2:]
    while len(b)<8:
        b='0'+b
    r=b.replace('1','2')
    r=r.replace('0','1')
    r = r.replace('2', '0')
    r=int(r,2)
    if r-i==-21:
        print(i)

for i in range(256):
    r=bin(i)[2:].zfill(8)
    r1=''
    for c in r:
       # r1+='1'if c=='0' else '0'
        if c=='0':
            r1+='1'
        else:
            r1+='0'
    if int(r1,2)-i==-21:
        print(i)
