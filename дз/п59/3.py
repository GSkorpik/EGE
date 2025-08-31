def delit(x):
    a=set()
    for i in range(1,x+1):
        if x%i==0:
            a.add(i)
    print(a)

x=int(input())
delit(x)