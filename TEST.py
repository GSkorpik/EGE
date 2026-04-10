f=[a,b,c,f,f,d,e,f,g]
mk=0
flag=1
k=0
a=set()
for i in f:
    if i.isalpha():
        k+=1
        a.add(i)
    else:
        if len(a)==7:
            if k > mk:
                mk = k
        flag=0
        k=0

print(mk)