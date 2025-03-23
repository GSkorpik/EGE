x=set()
for n in range(10,301):
    s=bin(n)[2:]
    r=s.replace('0','')
    f=int(r,2)
    print(n,s,r,f)
    x.add(f)
print(len(x))