def f(s,m):
    if s<=537: return m%2==0
    if m==0: return 0
    if m%2!=0:
        return f(s-4,m-1) or f(s//5,m-1)
    else:
        return f(s - 4, m - 1) and f(s // 5, m - 1)


#print('19)', *[s for s in range(538,100000) if f(s,2 )])
#print('20)',*[s for s in range(538,10000) if not(f(s,1))and f(s,3)])
print('20)',*[s for s in range(538,10000) if not(f(s,2))and f(s,4)])