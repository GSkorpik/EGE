def f(s, m):
    if s >= 33: return m % 2 == 0
    if m == 0: return 0
    if m % 2 != 0:
        return f(s + 3, m - 1) or f(s * 2, m - 1)
    else:
        return f(s + 3, m - 1) and f(s * 2, m - 1)


print('19)', *[s for s in range(1, 33) if f(s, 2)])
print('20)', *[s for s in range(1, 33) if not f(s, 1) and f(s, 3)])
print('21)', *[s for s in range(1, 33) if not f(s, 2) and f(s, 4)])


