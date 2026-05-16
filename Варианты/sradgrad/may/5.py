
rm=0
for n in range(1,1000):
    b=bin(n)[2:]
    if sum(map(int,b))%2==0:
        r='1'+b[2:]+'0'
    else:
        r='11'+b[2:]+'1'

    r=int(r,2)
    if r<744 and rm<=r:
        rm=r
        print(n,r)