
k=0
for s in open('9-214.csv'):
    a=sorted(map(int,s.split(',')))
    if len(a)==len(set(a)):
        if 2*a[2]==a[0]+a[4]==a[1]+a[3]:
            k+=1
print(k)