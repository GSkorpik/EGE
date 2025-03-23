for n in range(1,50):
    s=bin(n)[2:]
    k=s.count('1')
    if k%2==0:
        s+='0'
    else:
        s+='1'
    k=s.count('1')
    if k%2==0:
        s+='0'
    else:
        s+='1'
    r=int(s,2)
    print(r,n)
