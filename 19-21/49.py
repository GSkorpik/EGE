def f(a,s, m):
    if a+s<=20: return m % 2 == 0
    if m == 0: return 0
    if m % 2 != 0:
        return f(a,s - 1, m - 1) or f(a,(s+1) // 2, m - 1) or f(a-1,s,m-1) or f((a+1)//2,s,m-1)
    else:
        return f(a,s - 1, m - 1) and f(a,(s+1) // 2, m - 1) and f(a-1,s,m-1) and f((a+1)//2,s,m-1)


print('19)', *[s for s in range(11, 100) if f(10,s, 2)])
print('20)', *[s for s in range(11, 100) if not f(10,s, 1) and f(10,s, 3)])
print('21)', *[s for s in range(11, 100) if not f(10,s, 2) and f(10,s, 4)])


