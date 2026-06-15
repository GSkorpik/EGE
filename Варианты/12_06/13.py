from ipaddress import*

for i in ip_network('173.142.100.17/255.255.254.0',0):
    print(i)
