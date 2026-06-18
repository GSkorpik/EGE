
f=open('24-1.txt').readline()
print(f[100:200])
f=' '+f+' '
f=f.replace('+','*')
f=f.split('*')
k=0
m=0
print(f[:5])
for i in range(len(f)):
    if len(f[i])>0 and  ((len(f[i])>1  and f[i][0]!='0') or f[i]=='0'):

        if f[i].count('-')>0:
            inde=[ x for x in range(len(f[i])) if f[i][x]=='-' ]
            k+=len(f[i][:min(inde)])
            m = max(m, k)
            k=len(f[i][max(inde)+1:])
        else:
            k+=len(f[i])+1
            m=max(m,k-1)

    else:
        k=0

print(m)