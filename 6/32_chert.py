from turtle import *
#goto(0,0) начальное положение по умолчанию
k=30
for i in range (1):
    p = pos()   # считываем текущие координаты черепашки
    print(p)
    goto(p + (k*3, k*6))# сместиться на dx, dy
    p = pos()
    goto(p + (k*8, k*(-5)))
    p = pos()
    goto(p + (k*(-5), k*(-3)))
    p = pos()
    goto(p + (k*(-6), k*2))
up()
for x in range(0, 12):
  for y in range(-5, 8):
    goto(x*k, y*k)
    dot(4,"red")
