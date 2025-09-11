a=set()

for n in range(1,1000):
    b=bin(n)[2:]
    if n%2==1:
        r='1'+b+'11'
    else:
        r='11'+b+'00'

    r=int(r,2)
    if r<127:
        a.add(r)
print(max(a))