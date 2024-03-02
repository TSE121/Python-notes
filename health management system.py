# Health Management Problem
# Rohan , Harry, Hammand
# Total 6 files
import datetime


def getdate():
    return str(datetime.datetime.now())


# Choosing a User
user = int(input("Enter 1 for Rohan, 2 for Harry, 3 for Hammand:"))
mode = str(input("Choose diet or Exercise ")).lower()
if mode == "diet":
    eaten = str(input("What you ate:"))
    eaten = getdate() + " - " + eaten
elif mode == "exercise":
    exercise = str(input("What you exercised:"))
    exercise = getdate() + " - " + exercise 

if user == 1 and mode == "diet":
    with open("rohan-diet.txt", "a") as f:
        f.write(eaten)
        f.write(" \n")

elif user == 1 and mode == "exercise":
    with open("rohan-exercise.txt", "a") as f:
        f.write(exercise)
        f.write(" \n")

elif user == 2 and mode == "diet":
    with open("Harry-diet.txt", "a") as f:
        f.write(eaten)
        f.write(" \n")

elif user == 2 and mode == "exercise":
    with open("Harry-exercise.txt", "a") as f:
        f.write(exercise)
        f.write(" \n")

elif user == 3 and mode == "diet":
    with open("hammand-diet.txt", "a") as f:
        f.write(eaten)
        f.write(" \n")

elif user == 3 and mode == "exercise":
    with open("hammand-exercise.txt", "a") as f:
        f.write(exercise)
        f.write(" \n")
