
'''
print('x y z w | F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f= ((z <= y) and (not(x) <= w)) <= ((z == w ) or (y and not(x)))

                if f == 0:
                    print(x, y, z, w,  '|', f)

'''
'''
def f(n):
    alf='0123456789ab'
    s=''
    while n!=0:
        s=alf[n%12]+s
        n//=12
    return s

r1=0
for n in range(12,100):
    a=f(n)

    if n%12==0:
        r=a+a[-2:]

    else:
        k=(n%12)*9
        r=a+f(k)

    r=int(r,12)
    if r >300:
        print(r)

'''
'''
нет проблем
for x in range(1,100000):
    y=bin(4**1014-2**x+12)[2:]
    a=y.count('0')
    if a==2000:
        print(x)
'''
'''
нет проблем
import sys
sys.setrecursionlimit(2000)
def F(n):
    if n<7:
        return 7
    else:
        return n+1+F(n-2)
print(F(2024)-F(2020))
'''