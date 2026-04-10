f=open('24.txt').readline().strip()
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

print(mk)