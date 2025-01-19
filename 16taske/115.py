def F(n):
    if n<=1:
        return 1
    if n>1 and n%3==0:
        return 2*F(n-1)+F(n-2)
    else:
        return 3*F(n-2)+F(n-1)

def isPrime(n):
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            return False
    return True

k=0
for i in range(2, 35 + 1):
    if isPrime(sum(map(int,str(F(i))))):
        print(i)
        k+=1
print(k)