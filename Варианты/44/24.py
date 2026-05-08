f=open('24-181.txt').readline()
#f='AAAAA.AAAAAAA.AAAAAAaaaa.aaaa'

f=f.split('.')
m=0
for i in range(len(f)-1):
    l=len(f[i])+len(f[i+1])
    m=max(m,l+1)

print(m)