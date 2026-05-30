from ipaddress import*

k=0
for i in ip_network('234.151.74.12/255.255.128.0',0):
    #print(i)
    b=f'{i:b}'
    #print(b)
    if b.count('1')%7!=0:
        k+=1

print(k)