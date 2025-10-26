a=int(input())
b=int(input())
k=0
while a%4!=0:
    a+=1
if b%2!=0:
    b+=1
k1=a//4
while a!=(b-2):
    a=a+4
    b=b-2
    k+=1

print(k+k1)
