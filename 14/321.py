x=3**72+6*3**50-7*3**26+2*3**15+155
n=9
s=''
m=set()
while x!=0:
    a=x%n
    s=str(a)+s
    m.add(str(a))
    x//=n
print(len(m),len(s))