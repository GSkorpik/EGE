p=list(range(7,16))
q=list(range(12,26))
a=set()
for x in range(1000):
    Q = x in q
    P = x in p
    A = x in a
    if (((not P) or A) and (( not Q) or A)) == 0:
        a.add(x)
print(a)
              
