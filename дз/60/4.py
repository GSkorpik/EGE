def func(a,b):
    d=1
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            d=i
            break
    return d

a=int(input())
b=int(input())
print(func(a,b))