from ipaddress import*
k=0
ip=ip_address('188.214.176.0')
for mask in range(32):
    net=ip_network(f'188.214.176.25/{mask}',0)
    if net.num_addresses>=100 and net[0]==ip:
        k+=1
    print(mask,net,net.num_addresses)
print(k)
'''
156)	Для узла c IP-адресом 188.214.176.25 адрес подсети равен 188.214.176.0. 
Сколько существует различных возможных значений маски, если известно, что в этой сети не менее 100 узлов? Ответ запишите в виде десятичного числа.
'''