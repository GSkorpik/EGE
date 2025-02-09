x=int(input())#число в 10сист

n=int(input())#в какую систему перевлдим
#1 способ с цифрами

s=0
k=0
while x!=0:
    a=x%n
    s+=a#сумма цифр
    k+=1#кол-во цифр
    x//=n
    print(a)
print(s,k)

#2 способ перевода с помощью строки   (n<=10)
s=''
while x!=0:
    a=x%n
    s=str(a)+s
    x//=n
print(s)
print(int(s,n))
