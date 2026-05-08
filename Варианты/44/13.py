from ipaddress import*
ip=ip_address('117.157.2.8')
for a in range(32):
    net=ip_network(f'{ip}/{a}',0)

    if all(f'{ip:b}'[:16].count('1') >= f'{ip:b}'[16:].count('1') for ip in net):
        print(a,net.netmask)
