from turtle import*
k=10
screensize(1000,1000)
tracer(0)
left(90)

for i in range(10):
    for ii in range(3):
        forward(10*k)
        right(90)
        forward(10*k)
        right(270)
    right(90)
up()
for x in range(-20,100):
    for y in range(-40,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()


'''
Повтори 10 [ Повтори 3 [ Вперёд 10 Направо 90 
Вперёд 10 Направо 270] Направо 90]
Определите площадь получившейся фигуры в квадратных единицах.
'''