
f=open('24-153.txt').readline()
#f='DDDDDDCCDDDDDCCDD'
f=' '+f+' '


while ' D' in f:
    f=f.replace(' D',' ')

while 'D ' in f:
    f=f.replace('D ',' ')

f=f.replace('B',"A").replace('C',"A").replace('F',"A").replace('E',"A")

for i in range(1,100):
    if 'A'+('D'*i)+'A' in f:
        print(i)
        break




