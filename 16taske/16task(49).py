def F(n):
    if n<=3:
        return n
    if n%2==0 and n >3:
        return 2*n+F(n-1)
    else:
        return n*n+F(n-2)

k=0
for i in range(1,101):
    if F(i)%3==0:
        k+=1

print(k)