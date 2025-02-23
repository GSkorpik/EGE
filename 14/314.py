x= (7**160*7**90)-(14**150+2**13)
n=7
s=0
while x!=0:
    a=x%n
    if a!=6:
        s+=a
    x//=n

print(s)