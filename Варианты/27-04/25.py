
def d(n):
    a=set()
    for i in range(10,100):
        if n % i == 0:
            a.add(i)
    if len(a)>0:
        return a
    return False

for n in range(333555,777999+1):
    a=d(n)
    if a!=False and len(a)==35:
        print(n,min(a),max(a))
