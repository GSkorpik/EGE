a=[]
for n in range(1,1000):
    b=bin(n)[2:]
    b=b[::-1]
    r=b+b[-1]
    r=int(r,2)

    if r>99:
        a.append(n)
print(min(a))
