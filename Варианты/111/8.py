print(int(str(10**3),9), int(str(10**4),9))
def f(n):
    s=''
    while n!=0:
        a=n%9
        s=str(a)+s
        n//=9
    return s
k=0
for n in range(729,6561):
    s=f(n)
    c=1
    if s.count('6')<=2:
        for i in '24680':
            for ii in '24680':
                c*=((i+'6')  not in s and ('6'+ii) not in s)
        if c==1:
            k+=1

print(k)