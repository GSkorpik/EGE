

for x in range(1,100000):
    y = 5 ** 2026 + 7 * 5 ** 1013 + 107 - x
    k5=0
    k0=0
    while y!=0:
        a=y%6
        y//=6
        if a==5:
            k5+=1
        if a==0:
            k0+=1
    if k5-k0==28:
        print(x,k5,k0)
        break
