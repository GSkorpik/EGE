

def f(n):
    c=0
    while n!=0:
        a=n%17
        if a>9:
            c+=1
        n//=17
    return c
for x in range(1,10000):
    a=12*17**12+13*17**7-x
    if f(a)==9:
        print(x)