from turtle import Turtle,Screen
from Class import Brain
t=Turtle()
screen=Screen()
shape=t.shape("arrow")
speed=t.speed(0)
mode=screen.colormode(255)
colours=[(240, 239, 236), (235, 171, 91), (232, 205, 99), (139, 67, 87), (219, 115, 141), (237, 67, 46), (115, 183, 220), (22, 108, 185), (34, 143, 88), (19, 172, 217), (230, 239, 230), (184, 217, 159), (49, 162, 82), (242, 236, 238), (35, 80, 75), (146, 206, 212), (227, 235, 242), (241, 179, 144), (209, 59, 69), (122, 180, 136), (27, 72, 66), (228, 168, 183), (73, 120, 195), (159, 193, 229), (164, 86, 75), (177, 29, 44), (44, 75, 77), (132, 152, 88), (38, 66, 67)]
b=Brain(colours,t,screen)
b.start()
for _ in range(5):
    b.right()
    b.left()
b.write()
exit=screen.exitonclick()
