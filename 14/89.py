
a=8**1023+2**1024-3

s=bin(a)[2:]

print(sum(map(int,s)))
