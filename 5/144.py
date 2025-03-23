for n in range(1,50):
    s=bin(n)[2:]
    if n%2==0:
        s+='00'
    else:
        s+='11'
    r=int(s,2)
    if r>115:
        print(n,r)
        break