y=364

k=0
for n in range(2,11):
    s=''
    a=y
    while a!=0:
        x=a%n
        a//=n
        s=str(x)+s
    if len(set(s))==1:
        k+=n

print(k)

