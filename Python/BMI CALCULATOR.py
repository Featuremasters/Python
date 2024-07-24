age=int(input("Age\n"))
height=float(input("Height in feet\n"))
con=height*0.305
weight=float(input("Weight in kg\n"))
BMI=int(weight/con**2)
print(BMI)
if BMI < 18.5:
    print("Under weight")
elif BMI > 18.5 and BMI < 24.9:
    print("Healthy")
elif BMI >25 and BMI <29.9:
    print("Overweight")
else:
    print("Obesity")
    
