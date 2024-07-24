print ("Welcome to the tip calculator")
def Percent(a,b):
    if a==5:
        return float(b*5)/100
    elif a==10:
        return float(b*10)/100 
    elif a==12:
        return float(b*12)/100
    else:
        print("please enter the stipulated tip percentage")
        return Percent(float(input("How much percentage you like to tip us '5 10 12'? \n")),b)
bill=float(input("What was your bill?\n RS "))
per=float(input("How much percentage you like to tip us '5 10 12'? \n"))
tip=Percent(per,bill)
people=int(input("How many people to split the bill?"))
total=round(tip + bill,2)
split=round(total/people,2)
print(f"The amount RS {split} is split of RS {total} which is included with tip RS {tip} and bill RS {bill}")

