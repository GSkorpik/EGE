def t(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        return 1
    return 0

k=1
for a in range(1,1000):
    k=1
    for x in range(1,1000):
        k*=(t(a,9,x)<=((max(x+7,16)<=31)==(not (t(49,21,x)))))
    if k==1:
        print(a)



