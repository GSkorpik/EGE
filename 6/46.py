from turtle import*
k=30
screensize(10000,10000)
tracer(0)
left(90)

for i in range(20):
    for ii in range(4):
        forward(15*k)
        right(90)
    backward(20*k)
    right(90)
up()

for x in range(-30,30):
    for y in range(-40,40):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()
'''
Повтори 20 [ Повтори 4 [Вперёд 15 Направо 90]
Назад 20 Направо 90]
Найдите длину оставленного черепахой следа.
'''