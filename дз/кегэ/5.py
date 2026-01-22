def f(n):
    s=''
    while n!=0:

        a=n%3
        s=str(a)+s
        n//=3
    return s





for n in range(1,1000):
    s=f(n)
    if n%3==0:
        r=s+s[-2:]
    else:
        su=f((sum(map(int,s)))*3)
        r=s+su

    r=int(r,3)
    if r%2!=0 and r>208:

        print(r)


