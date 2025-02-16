y=804


for n in range(2,11):
    c=0
    a=y
    while a!=0:
        x=a%n
        a//=n
        if x==1:
            c+=1
    if c>=1:
        print(n)

