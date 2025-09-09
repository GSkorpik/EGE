
a=set()
for n in range(1,1000000):
    b=bin(n)[2:]
    if n%2==0:
        r='10'+b
    else:
        r='1'+b+'01'
    r=int(r,2)
    if r<1234567:
        a.add(r)
print(max(a))