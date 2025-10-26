n=int(input())
d1=int(input())
s1=int(input())
p1=int(input())
d2=int(input())
s2=int(input())
p2=int(input())
summ1=0
summ2=0
if s1>=n:
    summ1=p1*n
if s2>=n:
    summ2=p2*n

if s1>=n and s2<n:
    print(summ1)
    print(1)
elif s2>=n and s1<n:
    print(summ2)
    print(2)

if s1>=n and s2>=n:
    if d1==d2:
        if summ1==summ2:
            print(summ1)
            print(1)
            print(2)
        elif summ1<summ2:
            print(summ1)
            print(1)
        elif summ1<summ2:
            print(summ1)
            print(1)

    elif d1>d2:
        print(summ1)
        print(1)
    elif d1<d2:
        print(summ2)
        print(2)
