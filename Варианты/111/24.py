f=open('24-253.txt').readline()
#f='ACCADAADD'
f=f.replace('O','A').replace('D','C').replace('F','C')
k=0
m=0
for i in range(0,len(f)-2,3):
    if f[i:i+3]=='CAA' or f[i:i+3]=='CCA':
        k+=1
        m = max(m, k)
    else:
        k=0
k=0
for i in range(1,len(f)-2,3):
    if f[i:i+3]=='CAA' or f[i:i+3]=='CCA':
        k+=1
        m = max(m, k)
    else:
        k=0
k=0
for i in range(2,len(f)-2,3):
    if f[i:i+3]=='CAA' or f[i:i+3]=='CCA':
        k+=1
        m = max(m, k)
    else:
        k=0
print(m)