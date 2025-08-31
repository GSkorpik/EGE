def func(x):
    s=''
    alf='0123456789ab'
    while x!=0:
        s=alf[x%12]+s
        x//=12
    return s

x=int(input())

print(func(x))
print(int(func(x),12))