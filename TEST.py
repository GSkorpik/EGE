n='-123-4567-89-'
inde=[ x for x in range(len(n)) if n[x]=='-' ]
print(n[:min(inde)])
print(n[-3:])














'''
def f(n):
    a=[]
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            if str(i).count('53')==1 and p(i)==True and str(n//i).count('53')==1 and p(n//i)==True:
                a.append(i)
                a.append(n//i)
    return a

def p(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    return True

k=0

for n in range(4501347296,10**10):
    a=f(n)

    if len(a)==2:
        print(n,min(a))
        k+=1
    if k==5:
        break
'''