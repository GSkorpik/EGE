k=0
maxa=0
a=[int(x) for x in open('17.txt')]
a70=max(x for x in a if x%100==70 )
for i in range(len(a)-2):
    a1=a[i]
    a2=a[i+1]
    a3=a[i+2]
    summ=a1+a2+a3
    if a1>0 and a2>0 and a3>0 and summ<=a70:
        k+=1
        maxa=max(maxa,summ)

print(k,maxa)