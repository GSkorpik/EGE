from turtle import*
k=30
tracer(0)
screensize(10000,10000)
left(90)

for i in range(10):
    forward(15*k)
    right(60)
up()

for x in range(-20,30):
    for y in range(-20,40):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()
'''
Повтори 10 [Вперёд 15 Направо 60]
Сколько существует точек с целочисленными координатами, лежащими на получившемся контуре?
'''