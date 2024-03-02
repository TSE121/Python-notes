#exercise 2
#Guess the number game
#By Pipal Deka
guess = 5
number = 15


while (guess<=5):
    num = int(input("Enter a Number:"))
    guess -=1
    if guess > 0:
        print("You have", guess, " guesses left")
        if num > 15:
            print("Enter smaller number")
        elif num < 15:
            print("Enter Larger Number")
        else:
            print("YOU GUESSED IT RIGHT")
            break
    else:
        print("Game Over")
        break

