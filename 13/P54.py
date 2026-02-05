
from ipaddress import*
k=0
ip=ip_address('148.228.112.0') # создали обьект "адрес сети"
for i in range(31):
    net=ip_network(f'148.228.120.242/{i}',0)
    if net[0]==ip:
        print(bin(int(net.netmask)))
        print(int(bin(int(net.netmask))[18:26],2))

        
'''0b11111111111111111111000000000000
   240'''
