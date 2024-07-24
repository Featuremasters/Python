def d(a):
    if a == "swim" or a== "wait" or a== "left" or a=="right" or a=="blue" or a=="yellow" or a=="red":
        return 1
    else:
            return 0
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("WELCOME TO THE TREASURE ISLAND")
print("Your mission is to find the treasure")
way=input("Left or Right?\n").lower()
d(way)
while not d(way):
    print("Enter the right option")
    way=input("Left or Right?\n").lower()
if way =="left":
    next=input("Swim or Wait\n").lower()
    d(next)
    while not d(next):
        print("Enter the right option")
        next=input("Swim or Wait\n").lower()
    if next=="wait":
        door=input("Which door 'YELLOW' 'RED' 'BLUE'\n").lower()
        d(door)
        while not d(door):
            print("Enter the right option")
            door=input("Which door 'YELLOW' 'RED' 'BLUE'\n").lower()  
        if door == "red" or door == "blue":
            print("GAME OVER")
        else:
            print("YOU WIN")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")