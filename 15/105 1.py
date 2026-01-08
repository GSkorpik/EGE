def p(x):
    return 43<=x<=49
def q(x):
    return 44<=x<=53
def a(a1, a2, x):
    return a1<=x<=a2
m=0
for a1 in range(40,65):
    for a2 in range(a1+1, 65):
        for x in range(40, 65):
            if ((a(a1, a2, x)<=p(x))or q(x))==0:
                break
        else:
            #m = max(m,(a2-a1))
            if (a2-a1)>m:
                m=a2-a1
                print(a1,a2)
print(m)

P = list(range(43, 49+1))
Q = list(range(44, 53+1))
U = list(range(100))
A = U.copy()
for x in U:
  if (((x in A) <= (x in P)) or (x in Q)) == False:
    A.remove(x)
print(A)
print( len(A)-1 )
