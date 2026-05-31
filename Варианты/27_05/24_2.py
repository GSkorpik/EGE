f=open('24_28396.txt').readline()
f=f.replace('-','*')

#print(f)
f=f.split('*')
f=f[:30]
print(f[:30])

k=0
m=0
s=''
for c in f:
    if c!='' and  int(c)<10**9 and int(c)%2==1:
        c=int(c)
        s+=str(c)+'*'
        print(s,c)
    else:
        m = max(m, len(s) - 1)
        print(s,m)
        s=''

print(m)