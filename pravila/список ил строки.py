def f(n):
    s=str(n)
    a=set(s)
    b=list(map(int,s))
    if len(b)==len(a):
        return True
    else:
        return False
#программа для проверки не повторяющих чисел