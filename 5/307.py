a=set()
for x in range(4,100):
    n=bin(x)[2:]
    k=n.count('0')
    x=x-k
    n = bin(x)[2:]
    n=n[-3:]+n
    r=int(n,2)
    if r>224:
        a.add(r)
print(min(a))
