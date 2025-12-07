from turtle import *

screensize(800,800)
k = 40
tracer(0)
left(90)

for i in range(100):
    forward(10*k)
    right(180)
    forward(10 * k)
    right(198)
up()

for x in range(-20, 20):
  for y in range(-20, 20):
    goto(x*k, y*k)
    dot(4,"red")
exitonclick()


'''
исполнения следующий алгоритм:
Повтори 100 [Вперёд 10 Направо 180 Вперёд 10 Направо 198]
Определите, сколько различных отрезков нарисует Черепаха при выполнении данного алгоритма?
'''