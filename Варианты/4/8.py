
c=0
for i in range(10**5,10**6):
    k=0
    for ii in str(i):
        if int(ii)%2==0:
            k+=1
    if k==6:
        c+=1
''' 
   if len(str(c))>6:
        print('lose')
        break'''
print(c,len(str(c)))

#90625 k==1
#218750 k==2
#281250 k=3
#203125 k==4
#78125 k==5
#12500 k==6
