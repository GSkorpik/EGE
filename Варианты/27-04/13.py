from ipaddress import*
k=0
for i in range(32):
    net=ip_network(f'90.155.69.100/{i}',0)
    if net[0]==ip_address('90.155.69.0'):
        k+=1
print(k)
