from ipaddress import*
ip=ip_address('92.52.42.0')
for i in range(32):
    net=ip_network(f'92.52.42.52/{i}',0)
    if net[0]==ip:
        print(net.netmask)