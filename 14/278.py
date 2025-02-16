y=622
sumn=0
for n in range(2,11):
    s=''
    a=y
    while a!=0:
        x=a%n
        s=str(x)+s
        a//=n
    if len(s)%2==0:
        sumn+=n
print(sumn)