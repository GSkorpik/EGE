def f(n):
    alf='0123456789abcdefghijklmnopqrst'
    s=''
    while n!=0:
        s=alf[n%30]+s

        n//=30
    return s


k=0

for n in range(1,1000):
    s=f(n)
    ds = sum(int(char, 30) for char in s)
    if ds==1 or ds==0:
        k+=1
    r = ds * (n%10)

    for i in range(2,round(r**0.5)+1):
        if r%i==0:
            k+=1
            break
    print(n,s,ds,r,k)


