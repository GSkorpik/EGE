def f(s, m):
    if s%10==0: return m % 2 == 0
    if m == 0: return 0
    if m % 2 != 0:
        return f(s + 3, m - 1) or f(s +1, m - 1) or f(s+11,m-1)
    else:
        return f(s + 3, m - 1) and f(s +1, m - 1) and f(s+11,m-1)


print('19)', *[s for s in range(11, 100) if f(s, 2)])
print('20)', *[s for s in range(11, 100) if not f(s, 1) and f(s, 3)])
print('21)', *[s for s in range(11, 100) if not f(s, 2) and f(s, 4)])


print(12+ 14+ 22+ 24 +32 +34+ 42 +44 +52+ 54+ 62+ 64+ 72+ 74 +82+ 84 +92 +94)