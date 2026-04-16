m=1000000000
for n in range(1,1000):
    b=bin(n)[2:]
    b1=b+str((sum(map(int,b))%2))
    b2 = b1 + str((sum(map(int, b1)) % 2))
    r=int(b2,2)
    if r>253:
        m=min(m,n)
print(m)