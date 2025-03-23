def f(n):
    alf='0123456789ab'#12сист
    s=''
    while n!=0:
        s=alf[n%12]+s
        n//=12
    return s
