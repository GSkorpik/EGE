from ipaddress import*

m=0
for i in ip_network('204.252.0.0/255.255.0.0'):
    b=f'{i:b}'
    m=max(m,b.count('1'))
print(m)