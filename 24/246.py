def p(n):
    s=n[::-1]
    if n==s:
        return True
    else:
        return False


f=open('24-241.txt').readline()
m=0
#f='123454123321'
for i in range(len(f)-1):
    s=f[i]
    for ii in range(i+1,len(f)):
        s+=f[ii]
        if p(s)==True:
            m=max(m,len(s))
            print(m)
            break

print(m)
'''
Текстовый файл 24-241.txt состоит не более чем из 106 символов и содержит только латинские буквы A, B, C, D, E, F, O.
Определите длину самой длинной цепочки символов, которая является палиндромом.'''