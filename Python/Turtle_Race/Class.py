from turtle import Screen, Turtle
from tkinter import messagebox
class Format:
    def __init__(self,size,colort,y,bet):
        self.size=size
        self.colort=colort
        self.y=y
        self.bet=bet
        self.screen=Screen()
    def create(self,color,position):
        t=Turtle()
        t.shape("turtle")
        t.color(color)
        t.penup()
        t.goto(x=-200,y=position)
        return t
    def loop(self):
        import random
        tur=[self.create(color,position) for color,position in zip(self.colort,self.y)]
        race=True
        while race:
            for turtle in tur:
                turtle.forward(random.choice(range(1,10)))
                if turtle.xcor()>= 200:
                        if self.bet==turtle.pencolor():
                            messagebox.showinfo("Result",F"Congarts!The {turtle.pencolor()} turtle won the race and you won the bet.")
                        else:
                            messagebox.showinfo("Result",F"Oops! you lost the bet, {turtle.pencolor()} turtle won the race.")
                        race=False 
                        self.screen.exitonclick()
                        
