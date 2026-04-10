
for a in range(1,10000):
    k=1
    for x in range(1,1000):
        k*=(x%a==0) or ((120<=x<=210)<=((x%36!=0)or (x+a<=272)))
    if k==1:
        print(a)