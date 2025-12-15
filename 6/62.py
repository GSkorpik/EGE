from turtle import*
k=30
screensize(10000,1000)
tracer(0)
left(90)

for i in range(5):
    for ii in range(3):
        forward(2*k)
        right(270)
    forward(k*4)
up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()


'''
Повтори 5 [ Повтори 3 [ Вперед 2 Направо 270] Вперед 4]
Найдите минимальную площадь выпуклого многоугольника, включающего фигуру.
'''