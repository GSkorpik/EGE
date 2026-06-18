
a=int('63089875',22)
b=int('17051',22)
c=int('7503',22)
for x in range(22):
    a1=a+x*22**5
    b1=b+x*22**2
    c1=c+x*22
    if (a1+b1+c1)%21==0:
        print((a1+b1+c1)/21)