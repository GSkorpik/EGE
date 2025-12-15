from turtle import *
k=40
screensize(10000,10000)
speed(6)
left(90)

for i in range(151):
    forward(10*k)
    right(300)
    forward(20*k)
    right(300)
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()

'''
Повтори 151 [Вперёд 10 Направо 300 Вперёд 20 Направо 300]
Сколько раз Черепаха пройдет через начало координат? 
Факт расположения Черепахи в начале координат перед выполнением алгоритма за прохождение не считать.
'''