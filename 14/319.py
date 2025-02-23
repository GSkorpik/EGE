x=(64**25+4**10)-(16**20+32**3)
n=4
k=-1
while x!=0:
    a=x%n
    k+=1
    if a==2:
        print(k)
        break
    x//=n