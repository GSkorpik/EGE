
def f(n):
    a=[]

    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            a.append(i)
            a.append(n//i)
    if len(a)>0:
        return max(a)+min(a)
    else: return 0

k=0
for n in range(700000,10**10):
    m=f(n)
    if m%100==14:
        print(n,m)
        k+=1
    if k==5:
        break


