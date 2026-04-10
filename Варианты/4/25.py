
f=0

res=[]
for a in range(1,30):
    for b in range(1,30):
        x=2**a+2**b
        if a!=b and x>2000000:
            if [x,a+b] not in res:
                res.append([x,a+b])
res=sorted(res)
for i in res[0:5]:
    print(i)

