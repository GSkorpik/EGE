from turtle import*
k=40
screensize(10000,10000)
tracer(0)

for i in range(4):
    forward(9*k)
    left(270)
up()
for i in range(3):
    forward(k)
    left(270)
    forward(k)
    left(90)
down()
for i in range(2):
    forward(9*k)
    left(270)
    forward(11*k)
    left(270)
up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()

'''
Повтори 4 [Вперёд 9 Налево 270]
Поднять хвост
Повтори 3 [Вперёд 1 Налево 270 Вперёд 1 Налево 90]
Опустить хвост
Повтори 2 [Вперёд 9 Налево 270 Вперёд 11 Налево 270]
Определите, сколько точек с целочисленными координатами будут находиться точно на контуре объединения фигур, нарисованных Черепахой при выполнении данной программы.
'''