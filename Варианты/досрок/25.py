
def d(n):

    for i in range(17,n+1,10):
        if n%i==0:
            return i
    return False


k=0
for n in range(700000,100000000):
    if d(n)!=False:
        print(n,d(n))
        k+=1
    if k==5:
        break

