f=open('24_28396.txt').readline()
f=f.replace('-','*')

#print(f)
f=f.split('*')
print(f[:30])

k=0
m=0
for i in range(len(f)):
    s=f[i]

    if s!='' and  int(s)<10**9 and s[0]!='0' and int(s)%2==1 :
        k+=len(s)+1
        m=max(m,k-1)
    else:
        k=0
print(m)