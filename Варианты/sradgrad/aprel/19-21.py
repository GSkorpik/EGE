def f(s1,s2,m):
    if s1*s2>=415: return  m%2==0
    if m==0: return 0
    if s1+s2<415:
        if m%2!=0:
            return f(s1+3,s2,m-1) or f(s1+17,s2,m-1) or f(s1,s2+3,m-1) or f(s1,s2+17,m-1)
        else:
            return f(s1 + 3, s2, m - 1) and f(s1 + 17, s2, m - 1) and f(s1, s2 + 3, m - 1) and f(s1, s2 + 17, m - 1)


print('19)', *[s2 for s2 in range(1,52) if f(8,s2,2)])
print('20)', *[s2 for s2 in range(1,52) if not f(8,s2,1) and f(8,s2,3)])
print('21)', *[s2 for s2 in range(1,52) if not f(8,s2,2) and f(8,s2,4)])
