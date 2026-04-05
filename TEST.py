'''a=[132,111,133]
k=0
c=0
maxx=0
for i in range(len(a)-2):
   k+=1
   if int(a[i]+a[i+1]+a[i+2])%10==(k+k+1+k+2)%10:
       c+=1
       maxx=max(maxx,abs((int(a[i]+a[i+1]+a[i+2])-(k+k+1+k+2))))

print(c,maxx)'''
x=67
print((x%10)*10+((x%100-x%10)//10))