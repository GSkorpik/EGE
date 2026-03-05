def f(x,n,s=''):

    if x==n:
        print(s)
        return s[-2]=='1'

    elif x>n: return 0
    if x<n:return  f(x+1,n,s+'1')+f(x*2,n,s+'2')

print(f(3,20))