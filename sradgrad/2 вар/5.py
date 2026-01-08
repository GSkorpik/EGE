a=[]
for n in range(1,1000):
    b=bin(n)[2:]
    if n%5==0:
        b1=b+'11'
    else:
        b11=bin(n//5)[2:]
        b1=b+b11
    r=int(b1,2)

    if r>896 and n%2==0:
        a.append(n)
print(min(a))