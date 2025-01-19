def F(n):
    if n<=1:
        return n
    if n>1 and n%2==0:
        return 1+F(n//2)
    if n>1 and n%2==1:
        return 1+F(n+2)

print(F(16))
