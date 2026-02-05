from ipaddress import*

ip=ip_address('153.209.28.0')
for mask in range(32):
    net=ip_network(f'153.209.31.240/{mask}',0)
    if net[0]==ip:
        print(net.netmask)
'''
Для узла с IP-адресом 153.209.31.240 адрес сети равен 153.209.28.0. Чему равен третий слева байт маски? Ответ запишите в виде десятичного числа.
'''