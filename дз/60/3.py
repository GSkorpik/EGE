def func(a,b):

    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            d=i
    return d

a=int(input())
b=int(input())
print(func(a,b))