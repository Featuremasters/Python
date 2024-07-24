import random
from Hl_data import data 
from Hl_Art import logo,vs
print(logo)
def format(statement):
    name=statement['name']
    description=statement['description']
    country=statement['country']
    return F"{name},{description}, from {country}"
start=True
score=0
statement1=random.choice(data)
statement2=random.choice(data)
while start:
    ar=True
    while ar:
        statement2=random.choice(data)
        if statement1['name']== statement2['name']:
            statement2=random.choice(data)
            if statement1['name']!= statement2['name']:
                ar=False   
    follower1=statement1['follower_count']
    follower2=statement2['follower_count']
    ur=True
    while ur:
        print(F"Compare A: {format(statement1)}")
        print(vs)
        print(F"Against B: {format(statement2)}")
        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess=="a" or guess=="b":
            if follower1>follower2 and guess=='a':
                print("Your are Right!!")
                statement1=statement1
                score+=1
                ur=False
            elif follower2>follower1 and guess=="b":
                print("Your are Right!!")
                statement1=statement2
                score+=1  
                ur=False
            else:
                print('''You are Wrong! Better Luck,Next Time''')
                print(F'Your score is {score}')
                start=False
                ur=False
        else:
            print("Enter the right input") 
             
            
