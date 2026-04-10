from ipaddress import*

for mask in range(32):
    net=ip_network(f'212.145.124.210/{mask}',0)


    print(net.network_address,net.netmask,net.prefixlen)


