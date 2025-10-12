def d(n):
    k=0
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            if i in [2,3,5,7]:
                k+=1
            if n//i in [2,3,5,7]:
                k+=1
    if k==2:
        return True
    else: return False


for i in range(1,30):
    print(d(i),i)