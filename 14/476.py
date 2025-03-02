

for x in range(0,2031):
    y = 3 ** 100 -x
    s=''
    k=0
    while y!=0:
        a=y%3
        y//=3
        if a==0:
            k+=1
    if k==5:
        print(x)