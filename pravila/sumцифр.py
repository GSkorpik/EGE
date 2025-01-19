x=int(input())
s=0
while x!=0:
    a=x%10
    x//=10
    print(a)
    if a%2==0:
        s+=a
print(s)


x=str(s)
print(x)
print(sum(map(int, x)))#сумма цифр числа (строка)