def d(n):
    a=[]
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            a.append(i)
            a.append(n//i)
    return a
k=0
for n in range(1350050,10000000):
    a=d(n)
    if len(a)>0:
        for i in a:
            if str(i)[-2:]=='11' and i!=11:
                print(n,i)
                k+=1
                break
        if k==5: break


