from turtle import*
screensize(1000,1000)
tracer(0)
k=40
left(90)

for i in range(100):
    forward(10*k)
    right(180)
    forward(10*k)
    right(190)
up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(k*x,y*k)
        dot(4,'red')
exitonclick()




'''
Повтори 100 [Вперёд 10 Направо 180 Вперёд 10 Направо 190]
Определите, сколько различных отрезков нарисует Черепаха при выполнении данного алгоритма?
'''