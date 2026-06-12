from ipaddress import*

for i in ip_network('98.71.254.171/255.255.248.0',0):
    b=f'{i:b}'
    if b.count('1')%3==0:

        print(i)