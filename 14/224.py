a=3**3*7**69-70
s=''
while a!=0:
    x=a%7
    s=str(x)+s
    a//=7
y=set(s)
for z in y:
    print(z,s.count(z))
if len(s)== len(y):
    print('no')
else:
    print('yes')

