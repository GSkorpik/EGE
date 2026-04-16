from ipaddress import*
maxx=0
for i in ip_network('146.180.173.153/255.192.0.0',0):
    r=str(i)
    s=int(r.split('.')[0])+int(r.split('.')[1])+int(r.split('.')[2])+int(r.split('.')[3])
    maxx=max(maxx,s)

print(maxx)


