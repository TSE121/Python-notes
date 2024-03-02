# rock paper scisor
import random

a= str(input("enter R(Rock), P(Paper), S(Scicor) \n")).upper()

list =["R", "P", "S"]
computer = random.choice(list)
# print(computer)

if a == "R" and computer == "R":
    print("match tie")

elif a == "R" and computer == "P":
    print("You lost")

elif a == "R" and computer == "S":
    print("You won")

elif a == "P" and computer == "R":
    print("You won")

elif a == "P" and computer == "P":
    print("Match tie")

elif a == "P" and computer == "S":
    print("You Lost")

elif a == "S" and computer == "R":
    print("You lost")

elif a == "S" and computer == "P":
    print("You won")

elif a == "S" and computer == "S":
    print("match tie")
