
a=set()
for n in range(1,1000):
    b= bin(n)[2:]
    if n %3==0:
        r=b+b[-3:]
    else:
        t=(n%3)*3
        r=b+bin(t)[2:]
    r=int(r,2)
    if r>120:
       a.add(n)
print(min(a))