
def f(n):
    k=0
    while n!=0:
        a=n%9
        if a==0:
            k+=1
        n//=9
    return k
for x in range(1,3001):
    a=9**150+9**30-x
    if f(a)==122:
        print(x)
        break