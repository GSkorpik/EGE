#:: P = [192734; 220904], Q = [123456; 1345830], R = [734652; 1023456]
#          20     30             10         60          40      50
p=list(range(20,30))
q=list(range(10,60))
r=list(range(40,50))
a=set()

for x in range(1000):
    Q=x in q
    P= x in p
    R=x in r
    A=x in a
    if (Q<=((not P)<= ((not R) and (not A))<=(not Q)))==0:
        a.add(x)

print(a)
print(1345830-123456)