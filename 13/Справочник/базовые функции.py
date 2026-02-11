#импорт библиотеки
from ipaddress import*

# кол-во нулей в степени числа 2 == кол-во возможных айпи


ip=ip_address('148.228.112.0')
net = ip_network(f'{ip}/{mask}', 0)
print(net.netmask, net)

#чтобы перевести в двоичку айпи адрес
b=f'{ip:b}'


#для подбора маски
for mask in range(32):
    net=ip_network(f'175.122.80.13/{mask}',0)

    # Вывод адреса сети   маски      колво едеиниц
print(net.network_address,net.netmask,net.prefixlen)

# для написание определённого байта
print(str(mask).split('.')[3])

# айпи не широколиненный и не нулевой
if ip not in [net.network_address,net.broadcast_address]:
    print(True)