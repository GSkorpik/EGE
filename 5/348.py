for n in range(1000,10000):
    #2345
    n1=n//1000
    n2=n//100%10
    n3=n//10%10
    n4=n%10
    p1=n1*n2
    p2=n3*n4
    if p1>p2:
        s=str(p2)+str(p1)
    else:
        s=str(p1)+str(p2)

    if s=='1214':
        print(n)
