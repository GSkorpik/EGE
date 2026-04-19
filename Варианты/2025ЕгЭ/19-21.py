
def f(s,m):
    if s<=11: return m%2==0
    if m==0: return 0
    if s>11:
        if m%2!=0:
            return f(s-3,m-1) or f(s-7,m-1) or f(int((s/3)-((s/3)%1)),m-1)
        else:
            return f(s - 3, m - 1) and f(s - 7, m - 1) and f(int((s/3)-((s/3)%1)),m-1)


print('19)', *[s for s in range(12,50) if f(s,2) ])
print('20)', *[s for s in range(12,50) if not f(s,1) and f(s,3) ])
print('21)', *[s for s in range(12,50) if not f(s,2) and f(s,4)])