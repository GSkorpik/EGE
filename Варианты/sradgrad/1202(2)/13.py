from ipaddress import*
net= ip_network(f'16.128.25.3/255.255.224.0',0)
b=net.broadcast_address
print(b)
print(16+128+31+255)