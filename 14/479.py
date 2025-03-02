
for x in range(4101,8000):
    y = 3 ** 100 -x
    s=''
    k=0
    while y!=0:
        a=y%3
        y//=3
        if a==0:
            k+=1
    if k==1:
        print(x)