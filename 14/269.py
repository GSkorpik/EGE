y=1988
sumn=0
for n in range(2,11):
    #print('     n=',n)
    a=y
    x1=a%n
    #print(x1)
    a//=n
    f=0
    while a!=0:
        x2 = a % n
        #print(x2)
        a //= n
        if x1==x2:
            f=1
            #print('n=',n)
        x1=x2
    if f==0:
        sumn+=n

print(sumn)

