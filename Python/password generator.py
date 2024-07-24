import random
print("Welcome to the Password Generator")
l=int(input("How many letters need to be in your password\n"))
n=int(input("How many numbers need to be in your password\n"))
s=int(input("How many symbols need to be in your password\n"))
letters1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=[ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
collab=[letters1,symbols,numbers]
t=[]
for j in range(0,l):
            alignl=random.choice(letters1)
            t+=alignl
for k in range(0,n):
            align2=random.choice(numbers)
            t+=align2
for g in range(0,s):
            align3=random.choice(symbols)
            t+=align3
random.shuffle(t)
password="".join(t)
print(f"YOUR PASSWORD IS '{password}'")

        