from ipaddress import*
k=0
for i in ip_network('192.168.32.48/255.255.255.192',0):
    s=f'{i:b}'
    if s.count('1')%2==0 and s.count('1')%4!=0:
        k+=1

print(k)