from turtle import *
#t=Turtle()
#t.screen.setup(800, 800)# размер окна
screensize(800,800)
k = 50 # масштаб
speed(5)# speed(0) - самая большая скорость, speed(10) - самая минимальная скорость
#tracer(0)- без анимации
left(90) # в Python Черепаха смотрит вдоль положительного
         # направления оси абсцисс.
for i in range(15):
    forward( k*4 )  #backward - назад
    right(60) # left - поворот влево
up() # down()
# рисовать точки
for x in range(0, 9):
  for y in range(0, 8):
    goto(x*k, y*k)
    dot(4,"red")
exitonclick()

