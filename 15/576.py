'''p=list(range(128764,775638))
q=list(range(280932,894568))
r=list(range(754683,929872))'''
p=list(range(10,40))
q=list(range(20,50))
a=set()

for x in range(10000):
    Q = x in q
    P = x in p
    R = x in r
    A = x in a
    if ((not A)<=((P==Q)<=(R==Q)) )== 0:
        a.add(x)
print(a)
print(929872-280932-1)