
a=set()
for n in range(1,10000000):
    s1=0
    s2=0
    for i in str(n):
        if int(i)%2==0:
            s1+=int(i)
    for k in range(0, len(str(n)), 2):
        s2 += int(str(n)[k])

    if s1>s2:
        r=s1-s2
    else:
        r=s2-s1

    if r==28:
       a.add(n)

print(min(a))

