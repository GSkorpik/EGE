def p(x):
    return 10<=x<=30
def q(x):
    return 12<=x<=24
def a(a1, a2, x):
    return a1<=x<=a2
m=111111110
for a1 in range(5,35):
    for a2 in range(a1+1, 35):
        for x in range(5, 35):
            if (((p(x))and q(x))<=(a(a1, a2, x)))==0:
                break
        else:
            #m = max(m,(a2-a1))
            if (a2-a1)<m:
                m=a2-a1
                print(a1,a2)
print(m)

