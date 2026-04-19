from ipaddress import*

for i in ip_network('45.172.106.203/255.255.252.0',0):
    print(i)