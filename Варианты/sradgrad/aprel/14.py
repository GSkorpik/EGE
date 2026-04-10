def f(n):
    k=0
    while n!=0:
        a=n%13
        if a==0:
            k+=1
        n//=13
    if k%2==0:
        return False
    else: return True

maxx=0
for x in range(1,2000):
    a=12*13**12+11*13**7-x
    if f(a)==True:
        maxx=max(maxx,x)

print(maxx)