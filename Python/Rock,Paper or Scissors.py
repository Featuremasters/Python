import random
print("Welcome to the Rock,Paper,Scissors")
Rock='''       
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
def play():
    print("Press any key to exist")
    c=input("Type 'start' to start\n").lower()
    if c == "start":
        player=input("Choose 0 for Rock, 1 for Paper, 2 for Scissors\n")
        
        def loop(p):
            if p=="0":
                print(Rock)
            elif p=="1":
                print(Paper)
            elif p=="2":
                print(Scissors)
            else:
                print("Enter valid input")
                loop(input("type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
        loop(player)
        print("Computer Choice ")
        computer=random.randint(0,2)
        t=str(computer)
        loop(t)
        if player==t:
            print("Draw")
        elif player=="0" and computer==1:
            print("You Lose")
        elif player=="1" and computer==2:
            print("You Lose")
        elif player=="2" and computer==0:
            print("You Lose")
        else:
            print("You Win") 
        play()     
    else:
        print("Hope!you had Good Game") 
play()