from ipaddress import*
k=0

for i in ip_network(f'172.16.96.0/255.255.224.0'):
    b=f'{i:b}'
    if b.count('1')%2==0:
        k+=1

print(k)