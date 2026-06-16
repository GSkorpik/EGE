

for a in range(1,1000):
    f=1
    for x in range(1,10000):
        f*=((x%a==0)or((120<=x<=210)<=((x%53!=0)or (x+a<=417))))
    if f==1:
        print(a)
