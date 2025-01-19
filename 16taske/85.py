def F(n):
    if n==1:
        return 1
    if n>=2 and n%2==0:
        return F(n//2)+1
    if n>=2 and n%2==1:
        return F(n-1)+n

k=0
for i in range(1,100000):
    if F(i)==16:
        k+=1
        print(i)
print(k)