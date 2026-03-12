maxa=0
for a in range(1,10000):
    f=1
    for x in range(1,1000):
        f*=((x%25==0)<=((x%a!=0)<=(x%60!=0)))
    if f==1:
        maxa=max(maxa,a)
print(maxa)