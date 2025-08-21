a=[]
for n in range(1,1000):
    b= bin(n)[2:]
    if sum(map(int,b))%2==1:
        r=b+'11'
    else:
        r='11'+b
    r=int(r,2)
    if r>102:
        print(n)
        break