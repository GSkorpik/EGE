def p(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    return True

def d(n):
    k=0
    for i in range(2,round(n**0.5)+1):
        if n%i==0 and p(i)==True and p(n//i)==True and str(i).count('5')==1 and str(n//i).count('5')==1:
            k+=1
            m=max(i,n//i)

        if k>1:
            return 0
    if k==1:
        return m

k=0
for i in range(1324727+1,10**10):
    dele=d(i)
    if dele :
        print(i,dele)
        k+=1
    if k==5:
        break







