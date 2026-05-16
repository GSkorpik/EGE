def f(n):
    k=0
    while n!=0:
        a=n%19
        if a==18:
            k+=1
        n//=19
    return k



for x in range(1,1000):

    a=19**270+19**240+19**190+19**180-x
    if f(a)==177:
        print(x)
        break