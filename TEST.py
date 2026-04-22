


def f(n):
    s=''
    while n!=0:
        a=n%9
        s=str(a)+s
        n//=9
    if s[0] not in '26' and s[-1]!=s[-2]:
        return s
    else:
        return s

print(int(f(2356),9))
print(f(4782969),f(43046721))
print(int(str(10**6),9))
''''k=0
for n in range(4782969,43046721):
    k+=f(n)


print(k)'''