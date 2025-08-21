s='1357'
su=0
for n in range(10000,100000):
    o=oct(n)[2:]

    for c in s:
        o=o.replace(c,'2')
    o=o+str(n%8)
    r=int(o,8)
    o = oct(r)[2:]

    for c in s:
        o = o.replace(c, '2')
    o = o + str(r % 8)
    r = int(o, 8)


    if r%2023==0:
        su+=n
print(su)
