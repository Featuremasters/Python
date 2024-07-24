import random
from Hangman_art import word_list,stage,logo
print(logo)
choice=random.choice(word_list).lower()
disply=[]
lives=6
cluec=3
for j in range(len(choice)):
    disply+="_"
    s="".join(disply)
end=False
while not end:
    guess=input(f"Guess the letter in the {len(choice)} letter-word\n").lower()
    if guess in disply:
        print(f"You already guessed the letter '{guess}'")
    for ik in range(len(choice)):
        k=choice[ik]
        if guess==k:
            disply[ik]=k
        h="".join(disply)
    print(h)
    if guess not  in choice:
        lives-=1
        print(f"You guessed {guess} is not in the word" )
        print(stage[lives])
        if cluec>0:
            clue=input("Clue needed?Type 'YES' otherwise Tyoe 'ANY KEY'\n").lower()
            if clue=="yes":
                a=False
                while not a:
                    cl=list(choice)
                    c=random.choice(cl)
                    i=cl.index(c)
                    if disply[i]=="_":
                        disply[i]=c
                        gh="".join(disply)
                        print(gh)
                        a=True
                        cluec-=1
        else:
            print("You used the all the clue")   
    if "_" not in disply:
        end=True
        print("Congrats!YOU WON")          
    if lives==0:
        end=True
        print(f"The word is '{choice.upper()}'")
        print("Better luck,next time")

        