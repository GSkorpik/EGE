
for x in range(0,2031):
    y = 7**91+7**160-x
    s=''
    k=0
    while y!=0:
        a=y%7
        y//=7
        if a==0:
            k+=1
    if k==70:
        print(x)