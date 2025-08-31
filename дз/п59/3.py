'''
def delit(x):
    a=set()
    for i in range(1,x+1):
        if x%i==0:
            a.add(i)
    print(a)

x=int(input())
delit(x)
'''
def delit(x):
    a=set()
    for i in range(2,x//2+1):
        if x%i==0:
            a.add(i)

    return a

x=int(input())
print(len(delit(x))+2)