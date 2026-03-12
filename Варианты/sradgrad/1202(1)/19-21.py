def f(s,m):
    if s<=1207: return m%2==0
    if m==0: return 0
    if s>1207:
        if m%2!=0:
            return f(s-3,m-1)or f(s-5,m-1)or f(s//4,m-1)
        else:
            return f(s-3,m-1)  and  f(s-5,m-1) and f(s//4,m-1)


print('19)',*[s for s in range(1208,10000) if not(f(s,1)) and f(s,2)]) #TRUE
print('20)',*[s for s in range(1208,10000) if f(s,3) and not f(s,1)])
print('21)',*[s for s in range(1208,10000) if not(f(s,2)) and f(s,4)])