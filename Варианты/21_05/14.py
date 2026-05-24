def f(n):
    k=0
    while n!=0:
        a=n%11
        if a==0:
            k+=1
        n//=11
    return k

for x in range(1,3000):
    a=9*11**210+8*11**150-x
    if f(a)==60:
        print(x)