from turtle import*
k=40
screensize(1000,1000)
tracer(0)
left(90)

for i in range(9):
    forward(3*k)
    right(45)
    forward(3*k)
    left(90)
up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()

'''
Повтори 9 [ Вперед 3 Направо 45 Вперед 3 Налево 90 ]
Найдите минимальную длину линии, которой можно нарисовать эту фигуру.
'''