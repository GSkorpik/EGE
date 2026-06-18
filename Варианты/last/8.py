from itertools import*
k=0

for i in product('АЕКНТЦ',repeat=5):
    k+=1
    s=''.join(i)
    #print(s)
    if k==3893:
        print(s)
    if s[0] not in 'АЕК' and s.count('Т')>0:
        print(k)
        break









'''def f(n):
    s=''
    while n!=0:
        a=n%9
        s=str(a)+s
        n//=9
    return s

#6561
#59049
k=0
for n in range(6561,59049):
    n=f(n)
    if str(n).count('3')==2:
        s=str(n).replace('3','1').replace('5','1').replace('7','1')
        if '12' not in s and '21' not in s:
            k+=1

print(k)
'''