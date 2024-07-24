print("Thank you for choosing 'COVAI MOMOS'")
size = input("WHAT SIZE DO YOU WANT? S,M or L\n")
def loop(a):
    if a =="S"or a== "M" or a == "L":
        if a == "S":
            return 90
        elif a == "M":
            return 120
        elif a =="L":
            return 150
    else:
        print("Please give right size")
        return loop(input("WHAT SIZE DO YOU WANT? S,M or L\n"))
bill=loop(size)
sauce= input("do you want Sauce 'Y' or 'N'\n")
def l(b):
    if b=="Y" or b== "N":
        if b == "Y":
            return 10
        else:
            return bill
    else:
        print("Please enter right option")
        return l(input("'Y' or 'N'"))
extra=l(sauce)
cheese= input("do you want cheese 'Y' or 'N'\n")
if cheese=="Y":
   ex_cheese= l(cheese)
   total=bill+extra+ex_cheese
else:
    total=bill+extra
print(f"Thank you for the order, Your bill is RS{total}")