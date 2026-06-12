

f=open('24.txt').readline()
f=f.replace('3','1').replace('5','1').replace('7','1').replace('9','1')
f='1'+f+'1'
f=f.split('1')
#f=f[:2009]
for i in range(len(f)-2008):
    f1=f[i:i+2008]
    f1=''.join(f1)
    #print(f1)
    #print(f1.count('2022'))
    if f1.count('2022')>=2026:
        print(i,len(f1))