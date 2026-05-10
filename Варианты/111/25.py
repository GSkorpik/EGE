def d(n):
    a=[]
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            if p(i)==True:
                a.append(i)
            if p(n//i)==True:
                a.append(n//i)
    return a

def p(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0: return False
    return True
k=0
m=0
for n in range(356738,404321+1):
    f=d(n)
    if len(f)==2 and f[0]!=f[-1]:
        if f[0]*f[-1]==n:
            k+=1
            if abs(f[0]-f[-1])>m:
                m=abs(f[0]-f[-1])
                c=n


print(k,c)