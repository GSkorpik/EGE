
a=[]
for n in range(1,1000):
    b=bin(n)[2:]
    bit=b.count('1')%2
    if n%2==0:
        r='1'+b+str(bit)

    else:
        r=b+'0'+str(bit)
    r=int(r,2)
    if r>100:
        a.append((r,n))

print(sorted(a,reverse=False)[0])