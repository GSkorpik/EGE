
for x in range(0,2031):
    y = 6**260+6**160+6**60-x
    s=''
    k=0
    while y!=0:
        a=y%6
        y//=6
        if a==0:
            k+=1
    if k==202:
        print(x)