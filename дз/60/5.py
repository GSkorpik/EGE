def func(x):
    r=''
    x = str(x)
    for i in x[::-1]:
        r=r+str(i)
    return r

x=int(input())
print(func(x))