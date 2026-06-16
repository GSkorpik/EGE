from ipaddress import*
m=0
ip=ip_address('123.222.180.11')
for i in range(1,33):
    net=ip_network(f'{ip}/{i}',0)
    #print(net)
    if net.network_address==ip_address('123.222.180.0'):
        print(net.netmask)
        b=f'{net.netmask:b}'
        m=max(m,b.count('0'))
print(m)