from turtle import Turtle,Screen
import random
t=Turtle()
screen=Screen()
t.shape("arrow")
t.speed(0)
screen.colormode(255)
t.pensize(1.25)
density=int(input("How much spirograph need to be denser,'lower number have higher density': "))
for _ in range(int(360/density)):
    t.circle(100)
    t.seth(t.heading()+density)
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
screen.exitonclick()