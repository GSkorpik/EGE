x1='0123456789abcde'
y1='0123456789abcdefg'
for x in x1:
    for y in y1:
        a1='123'+x+'5'
        a2='67'+y+'9'
        if (int(a1,15)+int(a2,17))%131==0:
            print(x,y,(int(a1,15)+int(a2,17))//131)