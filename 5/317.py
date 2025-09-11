

a=set()
for n in range(3,1000):
    b=bin(n)[2:]
    if n%4==0:
        r=b+b[-2:]
    else:
        r=bin((n%4)*2)[2:]+b
    r=int(r,2)
    if r<68:
        a.add(n)
print(max(a))
