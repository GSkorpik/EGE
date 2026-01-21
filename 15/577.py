'''p=list(range(268764,775638))
q=list(range(128932,894568))
r=list(range(546831,929872))
A=set()
for x in range(1000000):
    Q = x in q
    P = x in p
    R = x in r
    if ((not A)<= ((P == Q )<= (R==Q))) == 0:
        A.add(x)
print(A)'''


p=list(range(20,40))
q=list(range(10,50))
r=list(range(30,60))
a=set()
for x in range(100):
    Q = x in q
    P = x in p
    R = x in r
    A = x in a
    if ((not A)<= ((P == Q )<= (R==Q))) == 0:
        a.add(x)
print(a)

#{20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 50, 51,
#52, 53, 54, 55, 56, 57, 58, 59}
#(929872-268764)-1
