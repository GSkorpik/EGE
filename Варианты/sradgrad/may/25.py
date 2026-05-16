def d(n):
    s=0
    k=0
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            s+=i+(n//i)
            if p(i)==True:
                k+=1
            if p(n//i)==True:
                k+=1
    return s+k


def p(n):

    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    return True
k=0
for n in range(4555705,10000000000000):
    if n%10!=3:
        if ((n-d(n))%100)==23:
            print(n)
            k+=1
    if k==5:
        break