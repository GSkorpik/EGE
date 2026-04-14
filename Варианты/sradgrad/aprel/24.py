
f =open('24.txt').readline()
d=[]
m=0
l=0
for r in range(len(f)):
    if f[r].isdigit():
        l=r+1
        d=[]
    elif f[r] not in d:
        d.append(f[r])
    if len(d)==26:
        m=max(m,r-l+1)

print(m)



'''f=open('24.txt').readline().strip()
mk=0
k=0
a=set()
for i in f:
    if i.isalpha():
        k+=1
        a.add(i)

    else:
        if len(a)==26:
            if k > mk:
                mk = k
        k=0
        a=set()

print(mk)'''