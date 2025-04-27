def f(s, m):
    if s >= 29: return m % 2 == 0
    if m == 0: return 0
    if m % 2 != 0:
        return f(s + 1, m - 1) or f(s * 2, m - 1) or f(s + 2, m - 1)
    else:
        return f(s + 1, m - 1) and f(s * 2, m - 1) and f(s + 2, m - 1)


print('19)', *[s for s in range(1, 29) if f(s, 1)])
print('20)', *[s for s in range(1, 29) if not f(s, 1) and f(s, 3)])
print('21)', *[s for s in range(1, 29) if not f(s, 2) and f(s, 4)])


