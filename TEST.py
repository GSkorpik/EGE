

f=open('24_23762.txt').readline()
#f='2025Y2025YGGYDDY2025YYYY2025'
f=f.split('Y')
#print(f)
m=0
for i in range(len(f)-80):
    f1=f[i:i+81]
    f1 = ''.join(f1)
    if f1.count('2025')>=90:
        m=max(m,len(f1)+80)
print(m)