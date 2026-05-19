k=0
c=[]
d=[200004, 200034, 200036, 200050, 200056]
for b in range(1,11):
    for a in range(103,100000000000000,103):
        s=a+3**b

        if s in d:
            print(s,b)

        if s>10**6:
            break
'''
        if 10**5<=s<10**6 and str(s).count('1')==0 and a%2!=0:
            c.append(s)
'''


c=sorted(c)
print(c[:5])