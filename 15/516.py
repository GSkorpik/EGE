b=list(range(10,41))
a=[]
k=0
for x in range(1,1000):
    if ((x in a) or ((x in b)<=(x%6!=0)))==0:
        a.append(x)
        k+=1
print(a[k-1]-a[0])