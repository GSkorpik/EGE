from ipaddress import*

for i in ip_network('146.180.173.153/255.192.0.0',0):
    print(i)