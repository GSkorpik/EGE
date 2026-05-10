def f(a,n):
    l=a[-1]
    if abs(l)>40 or a.count(l)>1: return 0
    if l==n: return 1

    return f(a+[l+2],n)+f(a+[l-3],n)


print(f([1],30))