print('''    
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
| |   ______     | || |   _____      | || |      __      | || |     ______   | || |  ___  ____   | | | |     _____    | || |      __      | || |     ______   | || |  ___  ____   | |
| |  |_   _ \    | || |  |_   _|     | || |     /  \     | || |   .' ___  |  | || | |_  ||_  _|  | | | |    |_   _|   | || |     /  \     | || |   .' ___  |  | || | |_  ||_  _|  | |
| |    | |_) |   | || |    | |       | || |    / /\ \    | || |  / .'   \_|  | || |   | |_/ /    | | | |      | |     | || |    / /\ \    | || |  / .'   \_|  | || |   | |_/ /    | |
| |    |  __'.   | || |    | |   _   | || |   / ____ \   | || |  | |         | || |   |  __'.    | | | |   _  | |     | || |   / ____ \   | || |  | |         | || |   |  __'.    | |
| |   _| |__) |  | || |   _| |__/ |  | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  \ \_  | | | |  | |_' |     | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  \ \_  | |
| |  |_______/   | || |  |________|  | || ||____|  |____|| || |   `._____.'  | || | |____||____| | | | |  `.___.'     | || ||____|  |____|| || |   `._____.'  | || | |____||____| | |
| |              | || |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------' ''')

import random
def choice():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    choice= random.choice(cards)
    return choice
def fchoice():
    c2choice=[cchoice]
    b=choice()
    c2choice.append(b)
    return c2choice
def add(cc):
    t= sum(cc)
    if t>21 and 11 in cc:
        if cc==uchoice:
            ask=input("DO YOU WANT TO CHANGE THE ACE TO 1,Type 'y' to yes,Type 'ANY KEY' to no: ").lower()
            if ask=="y":
                cc.remove(11)
                t=sum(cc)+1
                return t
        else:
            ask=random.choice(["y","n"])
            if ask=="y":
                cc.remove(11)
                t=sum(cc)+1
                return t
    return t
def win(you,computer):
    if computer==you:
        print("DRAW")
    elif computer>21:
        print("Computer Burst! You WON")
    elif you>21:
        print("You Burst!Computer WON")
    elif you>computer:
        print("You WON")
    elif computer>you:
        print("You Lose")
def s():
    print(f"your final hand: {uchoice}")
    cchoice=fchoice()
    you=add(uchoice)
    if add(cchoice)<17:
        cchoice.append(choice())
        print(f"Computer's final hand {cchoice}")
        computer=add(cchoice)
    else:
        print(f"Computer's final hand {cchoice}")  
    win(you,computer)
print("WELCOME TO THE BLACK JACK GAME")
sd=True
while sd:
    start=input("Type 'start' to start the game: ").lower()
    if start=="start":
        sd=False
        uchoice=[choice(),choice()]
        print(f"your card: {uchoice}")
        cchoice=choice()
        print(f"Computer's first card: {cchoice}")
        rotate=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if rotate== "y":
            uchoice.append(choice())
            s()
        elif rotate=="n":
            s()
    else:
        print("Enter the right input")
        