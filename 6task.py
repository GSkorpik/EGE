# Обязательная часть выполнения.
from turtle import*
lt(90)
s = 30
screensize(2000,2000)
tracer(0)
down()
# Редактируемая часть кода отвечающая за рисунок.
for i in range (4):
    fd(10*s)
    rt(60)
    fd(10*s)
    rt(120)

# написание точек.
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * s, y * s)
        dot(4,'red')
done()