from ipaddress import*
k=0
ip1=ip_address('176.213.225.119')
ip2=ip_address('176.213.195.58')
for i in range(33):
    net1=ip_network(f'{ip1}/{i}',0)
    net2=ip_network(f'{ip2}/{i}',0)
    if net1==net2:
        print(2**(31-i))