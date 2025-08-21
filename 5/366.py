def f(n):
    b=bin(n)[2:]
    while len(b)!=8:
        b='0'+b
    return b
s=0
for n in range(0,256):
    b=f(n)
    b=b.replace('0','2')
    b=b.replace('1','0')
    b=b.replace('2','1')
    if int(b,2)%5==0:
        r='100'+b[-5:]
    else:
        r = '101' + b[-5:]
    r=int(r,2)
    if r==180:
        s+=1
print(s)