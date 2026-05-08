import shutil

for n in range(1,100):
    b= bin(n)[2:]
    if b.count('1')%2==0:
        r='1'+b+'00'
    else:
        r='11'+b

    r=int(r,2)

    if r>=412:
        print(n)
        break