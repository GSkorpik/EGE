def F(n):
    if n<=1:
        return n
    if n>1 and n%2==0:
        return 1+F(n//2)
    else:
        return 1+F(n+2)#ветка без конца


for i in range(1,100000):#это использовать при бесконечной ветви
    try:
        r=F(i)
    except:
        pass
    else:
        print(i,F(i))
