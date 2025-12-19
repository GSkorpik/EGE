from turtle import*
k=40
screensize(10000,10000)
tracer(0)

for i in range(4):
    forward(10*k)
    right(90)
up()
right(90)
forward(5*k)
left(90)
down()
for i in range(4):
    forward(10*k)
    right(90)
up()
for x in range(-10,15):
    for y in range(-20,15):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()

'''
Повтори 4 [Вперёд 10 Направо 90]
Поднять хвост
Направо 90
Вперёд 5
Налево 90
Опустить хвост
Повтори 4 [Вперёд 10 Направо 90]
Определите, сколько точек с целочисленными координатами будет находиться на контуре пересечения фигур, нарисованных Черепахой при выполнении данной программы.
'''