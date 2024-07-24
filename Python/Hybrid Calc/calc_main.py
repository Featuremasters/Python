from calc_art import logo
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def divi(num1,num2):
    return num1/num2
def expression():
            exp=eval(input("Enter your expression with numbers(if necessary): "))
            return exp
def calc():
    operation={"+": add,"-": sub,"*": mul,"/": divi}
    number1=float(input("Enter the number to be calculated: "))
    flag=False
    while not flag:
        number2=float(input("Enter the number to be calculated: "))
        print("choose the operation")
        for i in operation:
            print(i)
        method=input("Type any of the above operation symbol to do the calculation: ")
        afunction= operation[method]
        answer=afunction(number1,number2)
        more=input("If you have more number to do the calculation, Type 'yes' or 'no': ").lower()
        if more=='yes':
            number1=answer  
        elif more=="no":
            flag=True
            print(f"The answer is {float(answer)}")
            sd=input("Do you want calculate the result of above result with your expression, Type'yes'or 'no': ").lower()
            inte=False
            while not inte:
                if sd=="yes":
                    exp =expression()
                    for i in operation:
                        print(i)
                    m=input("Type any of the above operation symbol to do the calculation: ")
                    efunction= operation[m]
                    ex=efunction((exp),answer)
                    print(f"The answer is {float(ex)}")
                    inte=True
                elif sd=="no":
                    print(float(answer))
                    inte=True
                else:
                    print("enter the right")
        else:
            print("Enter the right input")

print("WELCOME TO THE HYBIRD CALCULATOR")
print(logo)    
new=input("Do you want to calculate your expression or open calculator,Type 'yes' for expression.Type 'N' for calculator: ").lower()
if new=="yes":
    print(float(expression()))
else:
    calc()