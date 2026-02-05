from ipaddress import*

ip=ip_address('218.217.192.0')
for i in range(32):
    net=ip_network(f'218.217.212.15/{i}',0)
    if net[0]==ip:
        print(net.netmask)

'''
108)	Для узла с IP-адресом 218.217.212.15 адрес сети равен 218.217.192.0. Для скольких различных значений маски это возможно?
'''