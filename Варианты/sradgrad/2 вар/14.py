kmax=0
for x in range(1,7291):
    a=27**298+27**269-x
    k=0
    while a != 0:
        b = a % 27
        a //= 27
        if b == 0:
            k += 1
    if k > kmax:
        kmax = k
print(kmax)