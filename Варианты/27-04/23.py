from fnmatch import*

def f(x,n,s):
    if x==n:
        if fnmatch(s,'?A*CB?') and 'AA' not in s and 'BB' not in s and 'CC' not in s:
            return 1
    if x<n: return 0

    return f(x-1,n,s+'A')+ f(x-2,n,s+'B')+ f(x//2,n,s+'C')


print(f(34,2,''))