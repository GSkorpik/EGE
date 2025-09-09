a=set()
for n in range(1,1000):
    b=bin(n)[2:]
    s=b+str(sum(map(int,b))%2)
    s = s + str(sum(map(int, s)) % 2)
    r=int(s,2)
    if r>75:
        a.add(r)
print(min(a))