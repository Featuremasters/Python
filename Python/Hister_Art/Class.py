class Brain:
        def __init__(self,colours,t,screen):
                self.colours=colours
                self.t=t
                self.screen=screen
        def dot(self):
                import random
                for _ in range(10):
                        self.t.dot(20,random.choice(self.colours))
                        self.t.forward(50)
        def right(self):
                self.t.setheading(90)
                self.t.forward(50)
                self.t.setheading(0)
                self.t.forward(50)
                self.dot()
        def left(self):
                self.t.setheading(90)
                self.t.forward(50)
                self.t.setheading(180)
                self.t.forward(50)
                self.dot()
        def start(self):
                self.t.setheading(225)
                self.t.penup()
                self.t.forward(500)
                self.t.setheading(0)
        def write(self):
                self.t.goto(-100,300)
                self.t.write("HISER ART",move=True,align="center",font=("Arial",14,"bold"))
