y=3456


for n in range(2,11):
    b=0
    a=y
    while a!=0:
        x=a%n
        a//=n
        if a%2==1:
            b+=1

    if b < 1:
        print(n)
#ответ 23
