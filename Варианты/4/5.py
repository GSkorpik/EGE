def f(n):
    s=''
    while n!=0:
        a=n%5
        s=str(a)+s
        n//=5
    return s


for n in range(1,10000):
    s=f(n)
    if sum(map(int,s))%2==0:
        s=s+'222'
    else:
        s='33'+s+'4'
    r=int(s,5)
    if r<9616:
        print(n)