def pr(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    if n>1:
        return True

def d(n):
    a=set()
    for i in range(1,round(n**0.5)+1):
        if n%i==0:
            a.add(i)
            a.add(n//i)
    return sorted(list(a))

for i in range(10,100):
    print(i,d(i))
