#Create the turtle Angie which draws a circlular fractal

from random import random
import turtle

angie = turtle.Turtle()
angie.shape("arrow")
angie.color("blue")
angie.speed(20)
for i in range(1,37):
    angie.right(10)
    angie.circle(100)
window.exitonclick()
