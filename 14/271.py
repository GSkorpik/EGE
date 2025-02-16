x=17**5+85**8-10
n=17
c=0

while x!=0:
    a=x%n
    x//=n
    if a==16:
         c+=1
print(c)
