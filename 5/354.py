r1=0
for n in range(1,400):
    r=bin(n)[2:]
    r=r.replace('1','*')
    r=r.replace('0','1')
    r = r.replace('*', '0')
    s=r.count('1')
    if s%2==0:
        r=r+'0'

    else:
        r=r+'1'
    r=int(r,2)
    if r<170 and r>r1:
        r1=r
        n1=n
print(n1,r1)
