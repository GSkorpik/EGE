from ipaddress import*

n=ip_network('102.162.200.51/255.255.255.0',0)
print(n[-2])
print(102+162+200+254)