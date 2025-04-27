def f(s, m):
    if s >= 38: return m % 2 == 0
    if m == 0: return 0
    if m % 2 != 0:
        return f(s + 3, m - 1) or f(s * 2, m - 1) or f(s+1, m-1)or f (s+2,m-1)

    else:
        return f(s + 3, m - 1) and f(s * 2, m - 1)and f(s+1, m-1)and f (s+2,m-1)


print('19)', *[s for s in range(1, 38) if f(s, 2)])
print('20)', *[s for s in range(1, 38) if not f(s, 1) and f(s, 3)])
print('21)', *[s for s in range(1, 38) if not f(s, 2) and f(s, 4)])


