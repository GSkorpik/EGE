a=[int(x) for x in open('17.txt')]
s=sum(a)
c=0
maxx=0
for i in range(len(a)-2):

   s1=a[i]+a[i+1]+a[i+2]
   s2=i+1+i+2+i+3
   if s%10==(s2)%10:
       c+=1
       maxx=max(maxx,abs(s1-s2))

print(c,maxx)