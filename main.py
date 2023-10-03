from turtle import *
speed(15)
pensize(2)
bgcolor("black")
c=0
colour=["red","violet","white","blue","green"]
left(45)
for i in range(0,200):
    color(colour[c])
    forward(2*i)
    left(89)
    c=c+1
    if c>4:
        c=0
done()
