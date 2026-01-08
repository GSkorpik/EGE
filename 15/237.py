def p(x):
    return 133<=x<=177
def q(x):
    return 144<=x<=190
def a(a1, a2, x):
    return a1<=x<=a2
m=111111110
for a1 in range(120,200):
    for a2 in range(a1+1, 200):
        for x in range(120, 200):
            if (p(x)<=(( not(q(x)) and not(a(a1,a2,x))) <= (not(p(x))))) == 0:
                break
        else:
            #m = max(m,(a2-a1))
            if (a2-a1)<m:
                m=a2-a1
                print(a1,a2)
print(m)
