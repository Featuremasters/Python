#find the leap year
print("Welcome to Leap Year founder")
year=int(input("Enter the year to caluculate the Leap Year\n"))
if year% 4==0 and year%100!=0 or year%400 ==0:
    print(f"The year'{year}' is the 'LEAP YEAR'")
else:
    print(f"The year'{year}' is the 'NOT LEAP YEAR'")