
a=[int(x) for x in open('17_25356.txt')]
amax=max(int(x) for x in a if str(abs(x))[-2:]=='30')
k=0
maxx=0
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    if len(str(abs(a1)))!=4 and len(str(abs(a2)))!=4 and len(str(abs(a3)))!=4:
        summ=a1+a2+a3
        if summ>amax:
            k+=1
            maxx=max(maxx,summ)


print(k,maxx)