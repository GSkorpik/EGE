k=0
a=[int(x) for x in open('17_19900.txt')]
summ4=sum(int(x) for x in a if 999<abs(int(x))<10000)
mini=100000000000000000000000
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    ap=a1*a2*a3
    if (99<abs(a1)<1000)+(99<abs(a2)<1000)+(99<abs(a3)<1000)==2:
        if ap>summ4:
            k+=1
            mini=min(mini,ap)
print(k,abs(mini))
