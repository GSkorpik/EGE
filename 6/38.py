from turtle import *

screensize(800,800)
k = 30
tracer(0)
left(90)

for i in range(9):
    forward(10*k)
    right(80)
up()

for x in range(-20, 20):
  for y in range(-20, 20):
    goto(x*k, y*k)
    dot(4,"red")
exitonclick()



'''
исполнения следующий алгоритм:
Повтори 100 [Вперёд 10 Направо 80]
Определите, сколько отрезков проведёт Черепаха до возврата в исходную точку?
'''