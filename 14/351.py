s='123456789abc'
for x in s:
    a1 = x + '1418'
    a2 = '1' + x + '037'
    a3= '2'+x+('209')
    if int(a1,13)+int(a2,14)==int(a3, 19):
        print(int(a3, 19))
        break
