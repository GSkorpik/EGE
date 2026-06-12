def f(n):
    s=''
    while n!=0:
        a=n%11
        if a<10:
            s=str(a)+s
        else:
            s='A'+s
        n//=11
    return s
k=0
for n in range(1771561,19487171):
    s=f(n)
    a=set()
    for i in s:
        a.add(i)
    if len(a)==len(s):
        if all(x+'A' not in s for x in '02468') and all('A'+x not in s for x in '02468') :
            k+=1

print(k)




#print(int(str(10**6),11),int(str(10**7),11))