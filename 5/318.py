

a=set()
for n in range(3,10000):
    b=bin(n)[2:]
    if n%3==0:
        r=b+b[-3:]
    else:
        r=b+bin((n%3)*3)[2:]
    r=int(r,2)

    if r<68:
        a.add(r)
print(max(a))
