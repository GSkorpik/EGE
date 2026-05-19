from ipaddress import*

for i in ip_network('77.180.176.14/255.255.254.0',0):
    print(i)