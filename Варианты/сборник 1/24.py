f=open('24var01.txt').readline()

#f='1111111111advS55555abcS333BBCS11111BB'
f=f.split('S')
#print(f)
k=0
m=0

for i in range(1,len(f)):
    k=0
    for ii in '13579':
        k+=f[i].count(ii)

    if k==35:
        m=max(m,len(f[i])+1)
        print(f[i],len(f[i]),m )

print(m)