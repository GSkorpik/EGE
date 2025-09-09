a=set()

def f(n):
    s = ''
    if n==0:
        return '0'
    else:
        while n!=0:
            a=n%5
            s=str(a)+s
            n//=5

        return s

a=[]

for n in range(1,1000):
    s=f(n)

    if n % 2 == 0:
        r = s + f(int(s[-1]  * 3))

    else:
        r = s[-1] + s[1:-1] + s[0]+'1'



    r=r.lstrip('0')

    if r.count('0')==4:
        a.append(n)

print(min(a))
