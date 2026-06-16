def f(n):
    s=''
    while n!=0:
        a=n%13
        if a>10:
            if a==10:
                s='A'+s
            if a==11:
                s='B'+s
            if a==12:
                s='C'+s
        else:
            s=str(a)+s
        n//=13
    return s

k=0
for n in range(28561,371293):
    s=f(n)
    if 'A' not in s:
        k2=1
        for i in '02468C':
            for ii in '02468C':
                k2*=(i+ii not in s)
        if k2==1:
            for i in '13579B':
                for ii in '13579B':
                    k2 *= (i + ii not in s)
            if k2==1:
                a=set()
                for i in s:
                    a.add(i)
                if len(a)==len(s) and len (s)==5:
                    k+=1
                    #print(s)

print(k)






#print(int('10000',13), int('100000',13))
