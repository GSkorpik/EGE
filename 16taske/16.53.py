def F(n):
    if n>15:
        return n*n-5
    if n<=15 :
        return n*F(n+2)+n+F(n+3)

x=str(F(1))
print(F(1), sum(map(int, x)))
print(sum(map(int, '884415846')))