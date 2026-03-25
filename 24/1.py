

f=open('k7-02.txt')
f=f.readline()

c='C'
while c in f:
    c+='C'
print(len(c)-1)




'''#f='ABBBBBCCCBBBCCBBBBBBBBBBBCCAAAAA'
k=0
maxk=0
for c in f:
    if c=='C':
        k+=1
        if k>maxk:
            maxk=k
    else:
        k=0

print(maxk,str(f).count('C'))'''