from ipaddress import*
for i in ip_network('134.80.0.0/255.240.0.0',0):
    #print(i)
    b=f'{i:b}'
    if b.count('1')==b.count('0'):
        s=+sum(int(x) for x in b.split('.'))

print(s)