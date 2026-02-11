from ipaddress import*
maxa=0
for a in range(0,256):
    ip=ip_address(f'196.233.{a}.52')
    mask=ip_address('255.255.255.248')
    net=ip_network(f'{ip}/{mask}',0)
    if ip not in [net.network_address,net.broadcast_address]:

        if all(f'{ip:b}'[:16].count('1')>f'{ip:b}'[16:].count('1') for ip in net):
                print(a)
