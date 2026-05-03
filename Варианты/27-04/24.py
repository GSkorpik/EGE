
f=open('24-215.txt').readline()
#f='A1A1A1A1A1A1A1B2C3B3B333333A1B2C3C3C3'
f=f.replace('B','A').replace('C','A').replace('2','1').replace('3','1')
c='A1A'
k=1
while c in f:
    k+=1
    c+='A1A'
print((len(c)-3),k-1)
