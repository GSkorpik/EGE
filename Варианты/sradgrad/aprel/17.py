
a=[int(x) for x in open('17.txt')]
am=min(int(x) for x in a if x>0 and abs(x)%100==99)
k=0
minn=100000000
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    if (99<abs(a1)<1000) +(99<abs(a2)<1000)+(99<abs(a3)<1000)>=2:
        if (a1+a2+a3)>=am:
            k+=1
            minn=min(minn,a1+a2+a3)

print(k,minn)
