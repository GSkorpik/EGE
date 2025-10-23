

# Задача из 17-289
'''for i in range(len(a)-3):
    a4=a[i:i+4]

    if any(abs(x)%10==3 for x in a4) and \
            not(any(abs(x)%7==3 for x in a4)):
        k+=1
        mini=min(mini,max(a4)-min(a4))'''

'''# алгоритм евклида
a=int(input())
b=int(input())

while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)

'''
'''
#Задача 17-425
res=[]
aa=a[i:i+3]
if sum((x%11==a5) for x in aa)==1 and sum((x%7==a13) for x in aa)==1:
    res.append(sum(aa))
print(len(res),min(res))'''



