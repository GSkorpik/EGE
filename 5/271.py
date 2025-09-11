
a=set()
def func(n):
    s=''
    while n!=0:
        a=n%4
        s=str(a)+s
        n//=4
    return s
for n in range(1,1000):
    r=func(n)
    if n%2==1:
        r='2'+ r +'11'

    else:
        r='13'+ r +'02'

    r=int(r,4)
    if r>1000:
        a.add(r)

print(min(a))