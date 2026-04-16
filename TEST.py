
f='FFFFBCFFFFBCFFFFFFFFFFFBC'
bc=0
k=1
mk=0
for i in range(1,len(f)):
    k+=1
    if f[i-1:i+1]=='BC':
        bc+=1
    if bc<2:
        mk=max(mk,k)
    if bc>=2:
        k = 1
        bc = 0
        mk = max(mk, k )

print(mk)