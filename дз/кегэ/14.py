def f(n):
    k=0
    while n!=0:
        a=n%27
        if a==0:
            k+=1
        n//=27
    return k

for x in range(1,27000):
    a=3*27**9+2*27**6+27**3-x
    if f(a)==6:
        print(x)
        break
