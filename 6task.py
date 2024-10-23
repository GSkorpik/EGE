# Обязательная часть выполнения
from turtle import*
lt(90)
s = 30
screensize(2000,200)
tracer(0)
down()
# Редактируемая часть кода отвечающая за рисунок
for i in range (4):
    fd(10*s)
    rt(270)
up()
fd(3*s)
rt(270)
fd(5*s)
rt(90)
down()
for i in range(2):
    fd(10*s)
    rt(270)
    fd(12*s)
    rt(270)

# написание точек
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * s, y * s)
        dot(4,'red')
done()