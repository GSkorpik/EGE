nm=0
for n in range(1,1000):
    s=bin(n)[2:]
    if sum(map(int,s))%2==0:
        s=s+'0'
        s='10'+s[2:]
    else:
        s = s + '1'
        s = '11' + s[2:]
    r=int(s,2)
    if r<35 and nm<n:
        nm=n

print(nm)