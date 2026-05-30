def f(n):
    k=0
    b=0
    while n!=0:
        a=n%15
        if a==7:
            k+=1
        if a>10:
            if b==1:
                return False
            b=1
        if a<=10:
            b=0
        n//=15
    if k==1:
        return True


k=0
for n in range(50625, 759375):
    if f(n)==True:
        k+=1
print(k)



#print(int('10000',15),int('100000',15))
