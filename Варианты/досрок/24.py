f=open('24.txt').readline().strip()
#f='AAAAAAAAABCBCAFAAAAAABCAAAABCF'#22 18 18
b=[]
a=[i for i in range(len(f)) if f[i:i+2] == "BC"]

for i in range(len(a)-181):
    s=a[i+181]-a[i]
    b.append(s)


print(max(b))












'''
#f=open('24.txt').readline().strip()
f='AAAAAAAAABCBCAFAAAAAABCAAAABCF'#22 18 18
bc=0
k=1
mk=0
for i in range(1,len(f)):
    for ii in range(i+1,len(f)-1):
        k+=1
        if f[ii-1:ii+1]=='BC':
            bc+=1
        if bc<=2:

            mk=max(mk,k)

        if bc>2:
            print(k)
            #mk = max(mk, k)
            k = 1
            bc = 0
            break

print(mk)
'''

