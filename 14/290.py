for x in range(0,1000):
    y=oct(64**12-8**14+x)[2:]

    if y.count('7')==12 and y.count('1')==1:
        print(x)
        break
