def f(n):
    s=''
    while n!=0:
        a=n%6
        s=str(a)+s
        n//=6
    return s
mini=10**100
for x in range(0,2031):
    a=6**2030+6**100-x
    s=f(a)
    k=s.count('0')
    mini=min(mini,k)

print(mini)