k=0
for s in open('160.csv'):
    a=sorted(map(int,s.split(',')))
    if a[-1]<sum(a[:-1]) and a[0]+a[-1]==a[2]+a[1]:
        k+=1

print(k)