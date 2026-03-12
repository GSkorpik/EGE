
def f(s1,s2,m):
    if s1+s2>=211: return m%2==0
    if m==0: return 0
    if m%2!=0:
        return (s1+1,s2,m-1) or (s1*2,s2,m-1) or (s1,s2+1,m-1) or (s1,s2*2,m-1)
    else:
        return (s1 + 1, s2, m - 1) and (s1 * 2, s2, m - 1) and (s1, s2 + 1, m - 1) and (s1, s2 * 2, m - 1)


print('19)',*[s2 for s2 in range(1,194) if f(17,s2,2)])
print('20)',*[s2 for s2 in range(1,194) if not f(17,s2,1) and f(17,s2,3)])
print('21)',*[s2 for s2 in range(1,194) if not f(17,s2,2) and f(17,s2,4)])