s=0
for x in range(4,100):
    s=0
    a=(88+2*8**x)*8**x+88+8**8
    while a!=0:
        s+=a%8
        a//=8
    print(s,x)