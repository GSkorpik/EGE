def f(n):
    s=''
    k=0
    while n!=0:
        a=n%3
        if a==2:
            k+=1
        n//=3
    return k


a=9**8+3**24-6
print(f(a))