a=[]
for n in range(2,400):
    b=bin(n)[2:]
    r=b+b[-2]
    r=r+r[1]
    r=int(r,2)
    if r >=150 and r<=200:
        a.append(r)
print(len(a))