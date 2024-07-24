import random
print("Welcome to the Number Guessing Game")
number=random.choice(range(1,101))
print("I'm thinking of a number between '1 and 100'")
level=input("Choose the difficulty> Type 'Easy'  or 'Hard': ").lower()
if level=="easy":
    chance=10
elif level=="hard":
    chance=5  
win=False
while chance>0 and win==False:
    print(F"You have {chance} attempts reamining to guess the number") 
    guess=int(input("Make a guess"))
    if guess==number:
        print(F"You got it! The answer is '{number}'")
        win=True
    elif guess>number:
        if (guess-number)>=10:
            print("Too High")
        elif (guess-number)>=5:
            print("High")
        else:
            print("you need to guess near lower number ")
    elif guess<number:
        if (number-guess)>=10:
            print("Too Low")
        elif (number-guess)>=5:
            print("Low")
        else:
            print("you need to guess near higher number")
    chance-=1
if chance==0:
        print("You lost! No guesses remain")