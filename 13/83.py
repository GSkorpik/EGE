from ipaddress import*
ip=ip_address('115.12.64.0')
for i in range(32):
    net=ip_network(f'115.12.69.38/{i}',0)
    if net[0]==ip:
        print(net.netmask)
        a=bin(192)[2:]
        print(a.count('1')+16)
        break
'''
83)	Для узла с IP-адресом 115.12.69.38 адрес сети равен 115.12.64.0. Найдите наименьшее возможное количество единиц в двоичной записи маски подсети.
'''