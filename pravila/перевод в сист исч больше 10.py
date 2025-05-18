def f(n):
    alf='0123456789ab'#12сист
    s=''
    while n!=0:
        s=alf[n%12]+s
        n//=12
    return s
#Вариант 2
def f(n):
    a='0123456789ab'
    if n<12:
        return a[n]
    else:
        return f(n//12)+a[n%12]