x=87
for n in range(3,85+1):
    a= 87
    k=0
    while a!=0:
        a//=n
        k+=1
    if x%n==2 and k==2:
        print(n)
