from turtle import Screen
from tkinter import messagebox
from Class import Format
screen=Screen()
size=screen.setup(width=500,height=400)
colort=["blue","orange","red","green","yellow","pink","purple"]
y=[-150,-100,-50,0,50,100,150]
er=True
while er:
    bet=screen.textinput("Make your bet","which turtle will win the race? Enter a colour: ").lower()
    messagebox.showinfo("BET INFO",F"Your Bet is {bet} turtle ")
    f=Format(size,colort,y,bet)
    if bet in colort:
        f.loop()
        er=False  
    else:
        messagebox.showerror("Error","Enter the right input")