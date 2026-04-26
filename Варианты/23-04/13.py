from ipaddress import*
k=0
for i in ip_network('158.132.161.128/255.255.255.128',0):
    if int(str(i)[-1])%2==1:
        k+=1
print(k)