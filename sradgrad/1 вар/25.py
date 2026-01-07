def dele(n):
    d=set()
    for i in range(2,round(n**0.5)+1):
        if n %i==0:
            d.add(i)
            d.add(n//i)
    return sorted(list(d))
def p(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    if n>1: return True
def s(n):
    summ=0
    a=dele(n)
    for i in a:
        if p(i)==True:
            summ+=i
    if 0<summ<=30000 and summ%5==0:
        return True
    else:
        return False

k=0
for n in range(1325000-1,1,-1):
    if s(n)==True:
        print(n)
        k+=1
    if k==5:
        break