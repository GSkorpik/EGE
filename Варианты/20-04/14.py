
def f(n):
    k=0
    while n!=0:
        a=n%6
        if a==5:
            k+=1
        n//=6
    return k


a=36**17+6**66-216
print(f(a))