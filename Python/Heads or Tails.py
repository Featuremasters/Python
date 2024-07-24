import random
Toss=input("Heads or Tails\n").lower()
def revisit(Toss):
    if Toss=="heads" or Toss=="tails":
        rint=random.randint(0,1)
        if rint==1:
            p="heads"
            print("Heads")
        else:
            p="tails"
            print("Tails")
        if Toss==p:
            print("Congrats!!Won the TOSS")
        else:
            print("Sorry,Better luck next time")
    else:
     print("Enter the right input")
     revisit(input("Heads or Tails\n").lower())
revisit(Toss)