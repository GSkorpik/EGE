from turtle import*
k=60
screensize(10000,10000)
tracer(0)
left(90)
dot(6,'blue')

goto(-3*k,-4*k)

right(30)
for i in range(10):
    forward(14*k)
    right(120)
up()

for x in range(-20,100):
    for y in range(-20,100):
        goto(k*x,y*k)
        dot(4,'red')

exitonclick()

'''
Направо 30
Повтори 10 [Вперед 14 Направо 120] 
Определите, сколько точек с целочисленными отрицательными координатами будут находиться внутри полученного контура. 
Точки на линии не учитывать не следует.
'''