f=open('24-264.txt').readline()
import string

#f='AS0256DG124FB2NHF1643GH124GG22ABCDF942AACV'
alf=string.ascii_uppercase
for c in alf:
    f=f.replace(c,'A')
print(f)
for c in '0123456789':
    f =f.replace('A'+c,'A '+c).replace(c+'A',c+' A')
print(f)
a=[x if x[0]=='A' or x[0]!='0' and x[-1] not in '13579' else ' ' for x in f.split()]
print(a)
f=''.join(a)
print(f)
f=' '+f+' '
while 'A ' in f or ' A' in f:
    f=f.replace('A ',' ').replace(' A',' ')
print(f)
print(max(map(len,f.split())))
