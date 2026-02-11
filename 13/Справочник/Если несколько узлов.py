from ipaddress import*
ip=ip_address('111.3.160.0')
k=0
for i in range(32):
    net=ip_network(f'111.3.161.27/{i}',0)
    if net.num_addresses>=2000 and net[0]==ip:
        k+=1
print(k)
