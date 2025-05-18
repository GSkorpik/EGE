a=[]
for n in range(255):
    b=bin(n)[2:]
    s=sum(map(int,b))
    b=b+str(s%2)
    s = sum(map(int, b))
    r = b + str(s % 2)
    r=int(r,2)
    if r<114:
        a.append(r)
print(max(a))
