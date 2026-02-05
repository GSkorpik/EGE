# Автор В.Н. Шубинкин

from ipaddress import ip_network

for mask in range(16, 32):
    net1 = ip_network(f'151.172.115.121/{mask}', False)
    net2 = ip_network(f'151.172.115.156/{mask}', False)
    if net1 != net2:
        print(mask)
            
    
