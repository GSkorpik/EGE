y=572
sumn=0
for n in range(2,11):
    a=y
    x1=a%n
    a//=n
    while a!=0:
        x2 = a % n
        a //= n
        if x1==x2:
            sumn+=n

            break
            
        x1=x2

print(sumn)
