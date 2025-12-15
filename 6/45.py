from turtle import*
k=40
screensize(10000,10000)
tracer(0)
left(90)

for i in range(13):
    forward(10*k)
    right(90)
    forward(10*k)
    right(90)
    forward(30*k)
    right(90)
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(k*x,y*k)
        dot(4,'red')
exitonclick()


'''
Повтори 13 [Вперёд 10 Направо 90 Вперёд 10 
Направо 90 Вперёд 30 Направо 90]
Сколько точек с целочисленными координатами находится внутри полученного контура? 
Точки, лежащие на полученной линии, не считать.
'''