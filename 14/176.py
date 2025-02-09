a=9**17+3**16-27
'''
k0=0
k1=0
k2=0
while a!=0:
    x=a%3
    a//=3

    if x==0:
        k0+=1
    if x == 1:
        k1 += 1
    if x==2:
        k2+=1

print(k0,k1,k2)
'''
s=''
while a!=0:
    s=str(a%3)+s
    a//=3
print(s.count('0'),s.count('1'),s.count('2'))