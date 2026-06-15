def f(n):
    k=0
    while n!=0:
        a=n%27
        if a%2==0:
            k+=a
        n//=27
    return k



a=5*729**2024+3*243**1413-7*81**169-2*9**107+3017
print(f(a))
