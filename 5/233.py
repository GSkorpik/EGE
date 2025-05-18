s=0
for n in range(1000):
    b=bin(n)[2:]
    if b.count('1')> b.count('0'):
        b=b+'0'
    else:
        b=b+'1'
    k=len(b)
    if k%2==0:
        b=b[:k//2-1]+b[-(k//2-1):]
    else:
        b = b[:k // 2-1] +b[-(k // 2 - 1):]
    r=int(b,2)
    if r==58:
        s+=1
print(s)