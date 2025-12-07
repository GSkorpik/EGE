from turtle import *

screensize(800,800)
k = 10
tracer(0)
left(90)

for i in range(100):
    forward(10*k)
    right(30)
up()

for x in range(-20, 20):
  for y in range(-20, 20):
    goto(x*k, y*k)
    dot(4,"red")
exitonclick()

'''
исполнения следующий алгоритм:
Повтори 100 [Вперёд 10 Направо 30]
Определите, из какого количества отрезков будет состоять фигура, заданная данным алгоритмом.

'''