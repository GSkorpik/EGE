from turtle import*
screensize(1000,1000)
tracer(0)
k=40
left(90)

for i in range(7):
    left(60)
    forward(5*k)
    left(120)
    forward(5*k)
up()

for x in range(-10,20):
    for y in range(-10,20):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()


'''
Повтори 7 [Налево 60 Вперёд 5 Налево 120 Вперёд 5]
Определите, сколько точек с целочисленными координатами будут находиться внутри области,
ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.
'''