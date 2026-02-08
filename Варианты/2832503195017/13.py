from  ipaddress import*
for a in range(1,256):
    ip = ip_address('99.8.254.232')
    mask = ip_address(f'255.255.{a}.0')
    net = ip_network(f'{ip}/{mask}', 0)
    for ip in net[0]:
        b = f'{ip:b}'
        if b[0:16].count('1') <= b[16:32].count('1'):
            print(a)