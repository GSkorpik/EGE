def f(a,s,m):
    if s+a>=83: return m%2==0
    if m==0: return 0
    if m%2!=0:
        return f(a+1,s,m-1) or f(a,s+1,m-1) or f(a*4,s,m-1) or f(a,s*4,m-1)
    else:
        return f(a+1,s,m-1) and f(a,s+1,m-1) and f(a*4,s,m-1) and f(a,s*4,m-1)


print('19)', *[s for s in range(1, 78) if f(5,s, 1)])
print('20)', *[s for s in range(1, 78) if not f(5,s, 1) and f(5,s, 3)])
print('21)', *[s for s in range(1, 78) if not f(5,s, 2) and f(5,s,4)])