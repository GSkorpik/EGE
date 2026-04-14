from itertools import*


k=0
for x in product('0123456789AB',repeat=5):
    s=''.join(x)
    if s[0]!='0' and sum( c in '02468A' for c in s)==3:
        for d in '02468A':
            if d*3 in s:
                k+=1

print(k)





'''def f(n):
    k=0
    s=''
    while n!=0:
        a=n%12
        if a==10:
            a='a'
        if a==11:
            a='b'
        if a!='b':
            if a=='a':
                k += 1
                b = str(a)
            elif a%2==0 :
                k+=1
                b=str(a)
        s=str(a)+s
        n//=12
    if k==3:
        if (b*3) in s:
            return True
    else:return False

k=0
for i in range(20736,248831+1):
    if f(i)==True:
        k+=1
        print(f(i),i)
print(k)
print(int('10000',12))'''