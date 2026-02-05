
from ipaddress import *
for mask in range(32):
    net1=ip_network(f'152.217.69.70/{mask}',0)
    net2=ip_network(f'152.217.125.80/{mask}',0)
    if net1 == net2:
        print(net1,net1.netmask)
