'''f=open('24-221.txt').readline()
#f='00001110040000111411100000000000'
f=' '+f+' '
k=0
flag=0
m=0
f2=set()
for i in range(len(f)-1):

    if f[i]==f[i+1] and flag==0:
        k+=1
        f2.add(0)
    elif f[i]+f[i+1]=='01':
        k+=1
        flag=1

    elif f[i]==f[i+1] and flag==1:
        k+=1
        f2.add(1)
    else:

        if len(f2)==2:
            m=max(m,k+1)
        flag=0
        k=0
        f2=set()

print(m)'''


m=0
f=open('24-221.txt').readline()
#f='00001110040000111411100000000000'
for c in '23456789':
    f=f.replace(c,' ')
print(f)
f=f.replace('10','1 0').split()
print(f)
for i in f:
    if i.count('01')==1:
        m=max(m,len(i))
print(m)



