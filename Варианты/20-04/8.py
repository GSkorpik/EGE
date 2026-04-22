def f(n):
    s=''
    while n!=0:
        a=n%9
        s=str(a)+s
        n//=9
    if s[0] not in '26' and s[-1]!=s[-2]:
        return 1
    else:
        return 0

k=0
for n in range(531441,4782969):
    k+=f(n)


print(k)