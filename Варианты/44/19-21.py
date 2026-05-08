def f(s1,s2,m):
    if s1+s2>=75: return m%2==0
    if m==0: return 0
    else:
        if m%2!=0: return f(s1+3,s2,m-1) or f(s1,s2+3,m-1) or f(s1*2,s2,m-1) or f(s1,s2*2,m-1)
        else: return f(s1+3,s2,m-1) and  f(s1,s2+3,m-1) and f(s1*2,s2,m-1) and f(s1,s2*2,m-1)


print('19)',*[s2 for s2 in range(1,65) if f(9,s2,2)])
print('20)',*[s2 for s2 in range(1,65) if not f(9,s2,1) and f(9,s2,3)])
print('21)',*[s2 for s2 in range(1,65) if not f(9,s2,2) and f(9,s2,4)])
