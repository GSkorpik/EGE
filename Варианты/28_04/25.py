k=0
for i in range(87921,88187+1):
    s=sum(map(int,str(i)))
    if s%14==0:
        c=1
        for g in str(i):
           c*=int(g)
        if c%18==0 and c!=0:
            print(s,c)
