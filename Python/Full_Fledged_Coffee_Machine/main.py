from machine_art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 0,
}
money=0
def water(drink):
    data=MENU[drink]["ingredients"]
    iwater=data.get("water")
    if resources.get("water")>=iwater:
        return True
    print("Sorry,There is no enough Water")
    global er
    er=False
def milk(drink):
    data=MENU[drink]["ingredients"]
    imilk=data.get("milk")
    if resources.get("milk")>=imilk:
        return True
    print("Sorry,There is no enough Milk")
    global er
    er=False
def coffee(drink):
    data=MENU[drink]["ingredients"]
    icoffee=data.get("coffee")
    if resources.get("coffee")>=icoffee:
        return True
    print("Sorry,There is no enough Coffee")
    global er
    er=False
er=True
while er: 
    print("Welcome to the Covai Coffee House")
    print(logo)
    function=input("Customer or Maintainer: ").lower()
    if function=="maintainer":
        choice=input(" Type 'Secret word'for exceute the function: ").lower()
        if choice=="off":
            er=False
        elif choice=="report":
            print(F"Water: {resources['water']}")
            print(F"milk: {resources['milk']}")
            print(F"coffee: {resources['coffee']}")
            print(F'Money: ${money}')
    elif function=="customer":
        asd=True
        choice=input("What would you like to have? (espresso/latte/cappuccino): ").lower()
        if choice=="espresso":
            if water("espresso") and coffee("espresso"):
                asd=False
        elif choice=="latte":
           if water("latte") and milk("latte") and coffee("latte"):
               asd=False
        elif choice=="cappuccino":
            if water("cappuccino") and milk("cappuccino") and coffee("cappuccino"):
                asd=False
        if not asd:
            print("Please insert the coins, only quarters,dimes,nickles and pennies are accepted")
            quarters=int(input("How many quarter coins: "))
            dimes=int(input("How many dimes coins: "))
            nickles=int(input("How many nickles coins: "))
            pennies=int(input("How many pennies coins: "))
            total=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
            price=MENU[choice]["cost"]
            if total>=price:
                money+=price
                for i in resources.keys():
                    resources[i]-=MENU[choice]['ingredients'][i]
                if total>price:
                    print(F"Here is ${round(total-price,2)} dollars in change")
                print(F" Enjoy your '{choice}'")   
            else:
                print("Sorry,that's not enough money.Money refunded")
                er=False
    else:
        print("Sorry! your choice is not availble in our Menu.")