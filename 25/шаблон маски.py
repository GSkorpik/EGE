
# 1 способ
for i in '0123456789':
    for j in '0123456789':
        s=int(f'1{i}34567{j}9')
        if s%17==0:
            print(s,s//17)


#2 способ
for i in '0123456789':
    for j in '0123456789':
        s='1'+str(i)+'34567'+str(j)+'9'
        if int(s)%17==0:
            print(s,int(s)//17)

#3 способ
from fnmatch import *
for i in range(103456709,193456799+1):
    if fnmatch(str(i),'1?34567?9')and i%17==0:
        print(i,i//17)

