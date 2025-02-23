x=oct(8**20+((8**22-8**17)*(8**13+8**16)))[2:]
s= x.replace('7','0')
s=s[:-3]

ssum=sum(map(int,s))
print(ssum)